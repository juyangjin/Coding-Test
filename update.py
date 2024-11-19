import os
import subprocess
from urllib.parse import quote
import hashlib

# README 헤더 템플릿
HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
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

# 문제 난이도에 따른 정렬 우선순위 (숫자가 클수록 낮은 우선순위)
LEVEL_PRIORITY = {
    "0": 6,  # 레벨 0 (가장 낮은 우선순위)
    "1": 5,
    "2": 4,
    "3": 3,
    "4": 2,
    "5": 1,  # 레벨 5 (가장 높은 우선순위)
    "Bronze": 3,  # 백준 단계별 우선순위
    "Silver": 2,
    "Gold": 1,
}


def calculate_file_hash(file_path):
    """
    파일의 SHA256 해시값을 계산하여 반환합니다.
    - 이 함수는 README 파일의 변경 여부를 감지하는 데 사용됩니다.
    """
    if not os.path.exists(file_path):  # 파일이 없으면 None 반환
        return None
    with open(file_path, "rb") as f:  # 파일을 바이너리 모드로 읽기
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash


def generate_readme():
    """
    프로젝트 디렉토리 구조를 읽고 README.md 파일을 생성합니다.
    - 백준과 프로그래머스 문제를 분류하여 표로 출력합니다.
    - 새로 생성된 README와 기존 README의 내용을 비교해 변경 여부를 반환합니다.
    """
    print("Starting README generation...")  # 디버깅 메시지
    content = HEADER  # README 상단의 기본 헤더
    repo_name = "Coding-Test"  # 저장소 이름 (링크 생성에 사용)

    # 백준과 프로그래머스를 분류하기 위한 기본 구조
    problems = {
        "백준": {},  # 백준 문제 저장
        "프로그래머스": {},  # 프로그래머스 문제 저장
    }

    # 디렉토리 구조 탐색
    for root, dirs, files in os.walk("."):
        if root == ".":  # 최상위 디렉토리는 건너뜀
            continue

        parent_dir = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 이름
        if parent_dir not in problems:  # 백준/프로그래머스 외 디렉토리 건너뜀
            continue

        stage = os.path.basename(root)  # 난이도 또는 분류 정보 (ex: Bronze, Silver, etc.)

        if stage not in problems[parent_dir]:
            problems[parent_dir][stage] = {}

        for file in files:  # 현재 디렉토리 내 파일 탐색
            file_path = os.path.join(root, file)  # 파일 전체 경로
            relative_path = os.path.relpath(file_path, start=".")  # 상대 경로
            file_link = f"[{os.path.basename(file)}]({repo_name}/{quote(relative_path)})"

            problem_number = os.path.basename(os.path.dirname(root))  # 문제 번호

            if problem_number not in problems[parent_dir][stage]:
                problems[parent_dir][stage][problem_number] = {"languages": {}, "solution": None}

            # Markdown 파일은 해설로 처리
            if file.endswith(".md"):
                problems[parent_dir][stage][problem_number]["solution"] = file_link
            else:
                # 파일 확장자로 언어 감지
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")
                problems[parent_dir][stage][problem_number]["languages"][language] = file_link

    # README 본문 생성
    for category, stages in problems.items():
        content += f"## 📚 {category}\n"  # 카테고리 제목 추가

        # 난이도를 정렬하여 출력
        sorted_stages = sorted(
            stages.items(),
            key=lambda x: LEVEL_PRIORITY.get(x[0], 100),  # 우선순위로 정렬
            reverse=True
        )

        for stage, problems in sorted_stages:
            if not problems:  # 문제 없으면 스킵
                continue

            content += f"### 🚀 {stage}\n"
            content += "| 문제번호 | 해설 | 언어 |\n"
            content += "| -------- | ---- | ---- |\n"

            for problem_number, data in sorted(problems.items()):
                solution_link = data["solution"] if data["solution"] else "없음"
                language_links = " / ".join(
                    f"[{lang}]({link})" for lang, link in data["languages"].items()
                )
                if not language_links:  # 사용 언어가 없을 경우 "없음" 표시
                    language_links = "없음"

                # 표에 문제 정보 추가
                content += f"| {problem_number} | {solution_link} | {language_links} |\n"

    # 기존 README와 해시 비교
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as fd:
        fd.write(content)  # 새로운 README 작성

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:  # 내용이 동일하면 변경 없음
        print("No changes detected in README.md. Skipping commit and push.")
        return False

    print("README.md has been updated successfully.")
    return True


def commit_and_push():
    """
    변경된 README.md 파일을 Git에 커밋하고 원격 저장소에 푸시합니다.
    - Git 명령 실행 시 오류 발생 시 메시지를 출력합니다.
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
    """
    스크립트의 진입점:
    - README 파일을 생성하고 변경 사항이 있다면 Git에 푸시합니다.
    """
    if generate_readme():
        commit_and_push()
    else:
        print("No updates were made to README.md.")
