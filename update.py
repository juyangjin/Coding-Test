import os
import subprocess
from urllib.parse import quote
import hashlib
from collections import defaultdict

# README 헤더 템플릿
HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
이 저장소는 백준과 프로그래머스 문제 풀이를 정리한 저장소입니다.
"""

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
}

# 난이도 정렬 우선순위 (백준)
BOJ_DIFFICULTY_ORDER = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]

def calculate_file_hash(file_path):
    """파일의 SHA256 해시값을 계산하여 반환합니다."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

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

def extract_difficulty(directory_name, category):
    """
    디렉토리 이름에서 난이도를 추출합니다.
    :param directory_name: 디렉토리 이름
    :param category: 백준 또는 프로그래머스
    :return: 난이도 문자열
    """
    if category == "백준":
        for difficulty in BOJ_DIFFICULTY_ORDER:
            if difficulty.lower() in directory_name.lower():
                return difficulty
    elif category == "프로그래머스":
        for level in range(10):  # 난이도 0부터 9까지
            if f"level{level}" in directory_name.lower():
                return str(level)
    return "Unknown"

def generate_readme():
    """
    디렉토리 및 파일을 탐색하여 README.md를 생성합니다.
    """
    content = HEADER
    problems_by_difficulty = defaultdict(list)  # 난이도별 문제 저장

    for root, dirs, files in os.walk("."):
        dirs.sort()  # 디렉토리 정렬
        if root == ".":
            # 최상위 디렉토리에서 제외할 디렉토리
            for exclude in (".git", ".github"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        category = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 이름
        problem_dir = os.path.basename(root)  # 현재 디렉토리 이름
        problem_number, problem_name = split_problem_name(problem_dir)  # 문제 번호와 문제 이름 분리

        # 난이도 추출
        difficulty = extract_difficulty(problem_dir, category)

        # 문제 파일 탐색
        language_links = []
        for file in files:
            if file == "README.md":  # README.md는 문제 이름에만 사용
                continue
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_ext = os.path.splitext(file)[-1].lower()
            language = LANGUAGE_MAP.get(file_ext, "기타")
            language_links.append(f"[{language}]({quote(relative_path)})")

        if language_links:
            # 언어 링크를 알파벳순으로 정렬하고 슬래시로 구분
            language_links.sort()
            language_text = " / ".join(language_links)

            # README.md 링크 생성
            readme_path = os.path.join(root, "README.md")
            if os.path.exists(readme_path):
                problem_number_link = f"[{problem_number}]({quote(os.path.relpath(readme_path, start='.'))})"
            else:
                problem_number_link = problem_number

            # 문제 정보 저장
            problems_by_difficulty[(category, difficulty)].append(
                f"| {problem_number_link} | {problem_name} | {language_text} |\n"
            )

    # README 작성
    for (category, difficulty), problems in sorted(problems_by_difficulty.items(), key=lambda x: (x[0][0], BOJ_DIFFICULTY_ORDER.index(x[0][1]) if x[0][0] == "백준" else int(x[0][1]))):
        content += f"## 📚 {category} - {difficulty}\n| 문제번호 | 문제 이름 | 언어 |\n| ------ | --------- | ----- |\n"
        content += "".join(problems)

    # README 파일 작성
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)
    if not os.path.exists(readme_path):
        print(f"{readme_path} not found. Creating new README file...")
    with open(readme_path, "w") as f:
        f.write(content)

    current_hash = calculate_file_hash(readme_path)
    if previous_hash == current_hash:
        print("No changes detected in README.md. Skipping commit and push.")
        return False
    print("README.md has been updated successfully.")
    return True

def commit_and_push():
    """변경된 README.md 파일을 Git에 커밋하고 원격 저장소에 푸시합니다."""
    try:
        print("Adding README.md to Git...")
        subprocess.run(["git", "add", "README.md"], check=True)
        print("Committing changes...")
        subprocess.run(["git", "commit", "-m", "Update README.md"], check=True)
        print("Pushing to remote repository...")
        subprocess.run(["git", "push"], check=True)
        print("Changes have been pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during Git operation: {e}")
        print("Check Git setup or permissions and retry.")

if __name__ == "__main__":
    if generate_readme():
        commit_and_push()
    else:
        print("No updates were made to README.md.")
