#!/usr/bin/env python

import os
from urllib.parse import quote
import hashlib

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

# 난이도 순서 지정
BOJ_DIFFICULTY_ORDER = ["Bronze", "Silver", "Gold", "Platinum", "Ruby"]
PROGRAMMERS_DIFFICULTY_ORDER = ["0", "1", "2", "3", "4", "5"]

LANGUAGE_MAP = {
    ".py": "Python",
    ".cpp": "C++",
    ".java": "Java",
    ".kt": "Kotlin",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".cs": "C#",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".php": "PHP",
    ".c": "C",
    ".m": "Objective-C",
    ".r": "R",
    ".sql": "SQL",
}


def calculate_file_hash(file_path):
    """파일의 SHA256 해시값을 계산하여 반환합니다."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash


def extract_difficulty(problem_dir, category):
    """디렉토리 이름에서 난이도를 추출합니다."""
    if category == "백준":
        for difficulty in BOJ_DIFFICULTY_ORDER:
            if difficulty.lower() in problem_dir.lower():
                return difficulty
    elif category == "프로그래머스":
        for level in PROGRAMMERS_DIFFICULTY_ORDER:
            if problem_dir.startswith(level):
                return level
    return None


def split_problem_name(problem_name):
    """
    문제 번호와 문제 이름을 분리합니다.
    :param problem_name: 디렉토리 이름
    :return: 문제 번호 (왼쪽 숫자)와 문제 이름 (오른쪽 텍스트)
    """
    if ". " in problem_name:
        number, name = problem_name.split(". ", 1)
    elif "." in problem_name:
        number, name = problem_name.split(".", 1)
        name = name.strip()  # 이름 앞뒤 공백 제거
    else:
        number, name = problem_name, ""
    return number, name


def generate_readme():
    """
    디렉토리 및 파일을 탐색하여 README.md를 생성합니다.
    """
    content = HEADER
    problems_by_category = {
        "백준": {difficulty: [] for difficulty in BOJ_DIFFICULTY_ORDER},
        "프로그래머스": {level: [] for level in PROGRAMMERS_DIFFICULTY_ORDER},
    }

    for root, dirs, files in os.walk("."):
        dirs.sort()  # 디렉토리 정렬
        if root == ".":
            # 최상위 디렉토리에서 제외할 디렉토리
            for exclude in (".git", ".github", "images"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        category = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 이름
        problem_dir = os.path.basename(root)  # 현재 디렉토리 이름
        problem_number, problem_name = split_problem_name(problem_dir)  # 문제 번호와 문제 이름 분리

        # 난이도 추출
        difficulty = extract_difficulty(problem_dir, category)

        if category in problems_by_category and difficulty:
            problems_by_category[category][difficulty].append((problem_number, problem_name, files))

    # 카테고리와 난이도별로 README 내용 생성
    for category, difficulties in problems_by_category.items():
        content += f"## 📚 {category}\n"
        for difficulty, problems in difficulties.items():
            if problems:
                content += f"### 🚀 {difficulty}\n"
                content += "| 문제번호 | 문제 이름 | 언어 |\n"
                content += "| -------- | --------- | ----- |\n"

                for problem_number, problem_name, files in problems:
                    language_links = []
                    for file in files:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, start=".")
                        file_ext = os.path.splitext(file)[-1].lower()
                        language = LANGUAGE_MAP.get(file_ext, "기타")
                        language_links.append(f"[{language}]({quote(relative_path)})")
                    if language_links:
                        language_links.sort()
                        language_text = " / ".join(language_links)
                        content += f"| {problem_number} | {problem_name} | {language_text} |\n"

    # README 파일 작성
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)
    with open(readme_path, "w") as f:
        f.write(content)

    current_hash = calculate_file_hash(readme_path)
    if previous_hash == current_hash:
        print("No changes detected in README.md.")
        return False
    print("README.md has been updated successfully.")
    return True


if __name__ == "__main__":
    generate_readme()
