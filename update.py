#!/usr/bin/env python

import os
from urllib.parse import quote

# README 헤더
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

def main():
    """
    프로젝트 디렉토리에서 문제 목록을 탐색하고 README.md를 업데이트합니다.
    """
    content = ""
    content += HEADER

    # 처리된 디렉토리 및 문제 저장
    directories = []
    solved_problems = []

    for root, dirs, files in os.walk("."):
        # 최상위 디렉토리 제외
        if root == ".":
            for exclude in (".git", ".github"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        # 문제 카테고리 (디렉토리 이름)
        category = os.path.basename(os.path.dirname(root))  # 상위 폴더 이름
        problem_name = os.path.basename(root)  # 문제 폴더 이름

        # 카테고리별 README 섹션 시작
        if category not in directories:
            if category in ["백준", "프로그래머스"]:
                content += f"## 📚 {category}\n| 문제번호 | 문제 이름 | 언어 |\n| ------ | --------- | ----- |\n"
            else:
                content += f"### 🚀 {category}\n| 문제번호 | 문제 이름 | 언어 |\n| ------ | --------- | ----- |\n"
            directories.append(category)

        # 문제 파일 탐색
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_link = f"[{file}]({quote(relative_path)})"

            # 파일 확장자로 언어 추출
            file_ext = os.path.splitext(file)[-1].lower()
            language = LANGUAGE_MAP.get(file_ext, "기타")

            # 중복 방지
            if problem_name not in solved_problems:
                solved_problems.append(problem_name)

            # 문제 목록 추가
            content += f"| {problem_name} | {problem_name} | {language}: {file_link} |\n"

    # README 파일 작성
    with open("README.md", "w") as f:
        f.write(content)

    print("README.md has been updated.")

if __name__ == "__main__":
    main()
