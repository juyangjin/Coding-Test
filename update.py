import os
from urllib.parse import quote

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
    ".sql": "SQL",
}

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

def generate_readme():
    """
    디렉토리 및 파일을 탐색하여 README.md를 생성합니다.
    """
    content = HEADER
    directories = []  # 섹션별 디렉토리 목록 저장
    solved_problems = []  # 이미 처리된 문제 목록

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

        # 난이도 추출 (폴더 이름을 그대로 난이도로 사용)
        difficulty = problem_dir  # 폴더명이 난이도가 됨

        # README 섹션 작성
        if category not in directories:
            if category in ["백준", "프로그래머스"]:
                content += f"## 📚 {category}\n"
                directories.append(category)

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

            # 문제 정보를 추가
            content += f"### 🚀 {difficulty}\n"
            content += "| 문제번호 | 문제 이름 | 언어 |\n"
            content += "| -------- | --------- | ----- |\n"
            content += f"| {problem_number} | {problem_name} | {language_text} |\n"
            solved_problems.append(problem_dir)

    # README 파일 작성
    with open("README.md", "w") as f:
        f.write(content)

    print("README.md has been updated successfully.")
    return True

if __name__ == "__main__":
    generate_readme()
