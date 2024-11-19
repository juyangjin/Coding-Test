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
    categories = {}  # 카테고리별 문제를 저장할 딕셔너리

    for root, dirs, files in os.walk("."):
        dirs.sort()  # 디렉토리 정렬
        if root == ".":
            # 최상위 디렉토리에서 제외할 디렉토리
            for exclude in (".git", ".github"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        # 상위 디렉토리 이름을 카테고리로 사용 (백준, 프로그래머스)
        category = os.path.basename(os.path.dirname(root)) if os.path.dirname(root) != "." else None
        problem_dir = os.path.basename(root)  # 문제 폴더 이름
        problem_number, problem_name = split_problem_name(problem_dir)  # 문제 번호와 문제 이름 분리

        if category:
            # 카테고리별로 문제들을 분류
            if category not in categories:
                categories[category] = {}

            # 난이도별로 문제들을 분류
            difficulty = os.path.basename(os.path.dirname(root))  # 난이도는 문제 폴더의 상위 폴더명
            if difficulty not in categories[category]:
                categories[category][difficulty] = []

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

                # 문제 정보를 카테고리 및 난이도별로 저장
                categories[category][difficulty].append((problem_number, problem_name, language_text))

    # README 내용 작성
    for category, difficulties in categories.items():
        content += f"## 📚 {category}\n"  # 카테고리 헤더
        for difficulty, problems in difficulties.items():
            # 난이도 아이콘 설정
            if category == "백준":
                icon = "🚀"  # 백준은 로켓 아이콘
            else:
                icon = "⭐"  # 프로그래머스는 별 아이콘

            content += f"### {icon} {difficulty}\n"  # 난이도별 아이콘 추가
            content += "| 문제번호 | 문제 이름 | 언어 |\n"
            content += "| -------- | --------- | ----- |\n"

            for problem_number, problem_name, language_text in problems:
                content += f"| {problem_number} | {problem_name} | {language_text} |\n"

    # README 파일 작성
    with open("README.md", "w") as f:
        f.write(content)

    print("README.md has been updated successfully.")
    return True

if __name__ == "__main__":
    generate_readme()
