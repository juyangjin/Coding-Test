#!/usr/bin/env python

import os
from urllib.parse import quote
import hashlib

# README 헤더 템플릿
HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
이 저장소는 백준과 프로그래머스 문제 풀이를 정리한 저장소입니다.
"""

# 확장자별 언어 매핑
LANGUAGE_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".kt": "Kotlin",
    ".sql": "SQL",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".rb": "Ruby",
    ".go": "Go",
    ".php": "PHP",
    ".swift": "Swift",
    ".sh": "Shell",
    ".rs": "Rust",
}

def calculate_file_hash(file_path):
    """
    파일의 SHA256 해시값을 계산하여 반환합니다.
    """
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def main():
    """
    README.md를 생성하고 GitHub에 업데이트하는 스크립트.
    """
    print("Generating README...")  # 디버깅용 메시지
    content = HEADER

    # 처리된 디렉토리 및 문제 저장
    directories = []
    solved_problems = {}

    for root, dirs, files in os.walk("."):
        # 최상위 디렉토리 스킵 및 불필요한 폴더 제외
        if root == ".":
            for exclude in (".git", ".github"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        # 현재 디렉토리와 문제 이름 가져오기
        category = os.path.basename(os.path.dirname(root))  # 상위 폴더 이름
        problem_name = os.path.basename(root)  # 문제 폴더 이름

        # 중복 방지 및 카테고리 초기화
        if category not in directories:
            if category in ["백준", "프로그래머스"]:
                content += f"## 📚 {category}\n"
            else:
                content += f"### 🚀 {category}\n| 문제번호 | 문제 이름 | 언어 |\n| ------ | --------- | ----- |\n"
            directories.append(category)

        # 문제 데이터 초기화
        if category not in solved_problems:
            solved_problems[category] = {}

        # 파일 처리
        for file in files:
            file_ext = os.path.splitext(file)[-1].lower()
            language = LANGUAGE_MAP.get(file_ext, "기타")

            # 상대 경로 및 링크 생성
            relative_path = os.path.relpath(os.path.join(root, file), start=".")
            file_link = f"[{file}]({quote(relative_path)})"

            # 문제별 언어 추가
            if problem_name not in solved_problems[category]:
                solved_problems[category][problem_name] = {"languages": []}
            solved_problems[category][problem_name]["languages"].append((language, file_link))

    # README 내용 작성
    for category, problems in solved_problems.items():
        for problem, data in problems.items():
            languages = " / ".join(f"{lang}: {link}" for lang, link in data["languages"])
            content += f"| {problem} | {problem} | {languages} |\n"

    # README 파일 쓰기
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as f:
        f.write(content)

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:
        print("No changes detected in README.md. Skipping commit and push.")
        return False

    print("README.md has been updated successfully.")
    return True

if __name__ == "__main__":
    if main():
        print("README updated. You can add the commit and push logic here.")
    else:
        print("No updates were made to README.md.")
