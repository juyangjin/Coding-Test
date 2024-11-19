import os
import subprocess
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

# 문제 난이도에 따른 정렬 우선순위
LEVEL_PRIORITY = {
    "0": 6,
    "1": 5,
    "2": 4,
    "3": 3,
    "4": 2,
    "5": 1,
    "Bronze": 3,
    "Silver": 2,
    "Gold": 1,
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

def generate_readme():
    """
    프로젝트 디렉토리 구조를 읽고 README.md 파일을 생성합니다.
    """
    print("Starting README generation...")  # 디버깅 메시지
    content = HEADER
    repo_name = "Coding-Test"

    problems = {
        "백준": {},
        "프로그래머스": {},
    }

    # 최상위 디렉토리에서 백준과 프로그래머스 폴더를 처리하도록 수정
    for root, dirs, files in os.walk("."):
        # 최상위 디렉토리는 건너뛰지 않음
        if root == ".":
            continue

        # 최상위 디렉토리가 백준 또는 프로그래머스인 경우만 처리
        parent_dir = os.path.basename(os.path.dirname(root))  # 부모 디렉토리(백준, 프로그래머스)
        print(f"Root: {root}, Parent Dir: {parent_dir}")  # 디버깅: 현재 경로와 부모 디렉토리

        if parent_dir not in problems:  # 백준 또는 프로그래머스 디렉토리가 아니면 건너뜀
            continue

        stage = os.path.basename(root)  # 난이도 (예: Bronze, Silver 등)
        print(f"Stage: {stage}")  # 디버깅: 탐색된 난이도

        if stage not in problems[parent_dir]:
            problems[parent_dir][stage] = {}

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_link = f"[{os.path.basename(file)}]({repo_name}/{quote(relative_path)})"
            print(f"File: {file}, Link: {file_link}")  # 디버깅: 파일 이름과 생성된 링크

            problem_number = os.path.basename(os.path.dirname(root))  # 문제 번호

            if problem_number not in problems[parent_dir][stage]:
                problems[parent_dir][stage][problem_number] = {"languages": {}, "solution": None}

            if file.endswith(".md"):  # 해설 파일이면
                problems[parent_dir][stage][problem_number]["solution"] = file_link
            else:  # 언어별 파일 처리
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")
                problems[parent_dir][stage][problem_number]["languages"][language] = file_link

    # README 내용 작성
    for category, stages in problems.items():
        content += f"## 📚 {category}\n"

        sorted_stages = sorted(
            stages.items(),
            key=lambda x: LEVEL_PRIORITY.get(x[0], 100),
            reverse=True
        )

        for stage, problems in sorted_stages:
            if not problems:
                continue

            content += f"### 🚀 {stage}\n"
            content += "| 문제번호 | 해설 | 언어 |\n"
            content += "| -------- | ---- | ---- |\n"

            for problem_number, data in sorted(problems.items()):
                solution_link = data["solution"] if data["solution"] else "없음"
                language_links = " / ".join(
                    f"[{lang}]({link})" for lang, link in data["languages"].items()
                )
                if not language_links:
                    language_links = "없음"

                content += f"| {problem_number} | {solution_link} | {language_links} |\n"

    # README.md가 없으면 새로 만들기
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    if not os.path.exists(readme_path):
        print(f"{readme_path} not found. Creating new README file...")

    with open(readme_path, "w") as fd:
        fd.write(content)

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:
        print("No changes detected in README.md. Skipping commit and push.")
        return False

    print("README.md has been updated successfully.")
    return True

def commit_and_push():
    """
    변경된 README.md 파일을 Git에 커밋하고 원격 저장소에 푸시합니다.
    """
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
