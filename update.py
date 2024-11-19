import os
import subprocess
from urllib.parse import quote
import hashlib

# README 헤더 템플릿
HEADER = """# 백준 및 프로그래머스 문제 풀이 목록
이 저장소는 백준과 프로그래머스 문제 풀이를 정리한 저장소입니다.

## 목차
- [백준](#📚-백준)
- [프로그래머스](#📚-프로그래머스)
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

# 난이도별 우선순위 설정
LEVEL_PRIORITY = {
    "Bronze": 6,
    "Silver": 5,
    "Gold": 4,
    "Platinum": 3,
    "Diamond": 2,
    "Ruby": 1,
    "0": 6,
    "1": 5,
    "2": 4,
    "3": 3,
    "4": 2,
    "5": 1,
}


def calculate_file_hash(file_path):
    """파일의 SHA256 해시값을 계산합니다."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def generate_readme():
    """백준 및 프로그래머스 문제 디렉토리를 읽어 README.md 파일을 생성합니다."""
    print("Generating README...")
    content = HEADER
    repo_name = os.path.basename(os.getcwd())  # 현재 디렉토리 이름을 저장소 이름으로 사용

    problems = {"백준": {}, "프로그래머스": {}}

    for root, dirs, files in os.walk("."):
        if root == ".":
            continue  # 최상위 디렉토리는 건너뜀

        base_dir = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 (백준/프로그래머스)
        if base_dir not in problems:
            continue

        level = os.path.basename(root)  # 난이도 디렉토리 (예: Bronze, 0 등)
        if level not in problems[base_dir]:
            problems[base_dir][level] = {}

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_link = f"[{os.path.basename(file)}](./{quote(relative_path)})"

            problem_id = os.path.basename(os.path.dirname(root))  # 문제 번호

            if problem_id not in problems[base_dir][level]:
                problems[base_dir][level][problem_id] = {"languages": {}, "solution": None}

            # 설명.md 파일은 해설로 처리
            if file.endswith(".md"):
                problems[base_dir][level][problem_id]["solution"] = file_link
            else:
                # 파일 확장자로 언어 감지
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")
                problems[base_dir][level][problem_id]["languages"][language] = file_link

    # 카테고리별 README 내용 생성
    for category, stages in problems.items():
        content += f"\n## 📚 {category}\n"

        sorted_stages = sorted(
            stages.items(),
            key=lambda x: LEVEL_PRIORITY.get(x[0], 100),  # 우선순위 기준 정렬
            reverse=True
        )

        for stage, stage_problems in sorted_stages:
            if not stage_problems:
                continue

            content += f"### 🚀 {stage}\n"
            content += "| 문제번호 | 해설 | 언어 |\n"
            content += "| -------- | ---- | ---- |\n"

            for problem_id, data in sorted(stage_problems.items()):
                solution_link = data["solution"] or "없음"
                language_links = " / ".join(
                    f"[{lang}]({link})" for lang, link in data["languages"].items()
                ) or "없음"

                content += f"| {problem_id} | {solution_link} | {language_links} |\n"

    # README 파일 생성 및 변경 감지
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as fd:
        fd.write(content)

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:
        print("README.md에 변경 사항이 없습니다.")
        return False

    print("README.md가 성공적으로 생성되었습니다.")
    return True


def commit_and_push():
    """변경된 README.md를 Git에 커밋하고 푸시합니다."""
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "Update README.md"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("README.md가 성공적으로 푸시되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"Git 작업 중 오류 발생: {e}")


if __name__ == "__main__":
    if generate_readme():
        commit_and_push()
    else:
        print("README.md 업데이트가 필요하지 않습니다.")
