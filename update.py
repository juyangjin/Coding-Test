#!/usr/bin/env python

import os
from urllib.parse import quote

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

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

# 난이도/단계별 정렬 우선순위 (내림차순 정렬을 위해 높은 숫자가 쉬운 단계)
LEVEL_PRIORITY = {
    "0": 6,  # 프로그래머스 레벨 0
    "1": 5,  # 프로그래머스 레벨 1
    "2": 4,  # 프로그래머스 레벨 2
    "3": 3,  # 프로그래머스 레벨 3
    "4": 2,  # 프로그래머스 레벨 4
    "5": 1,  # 프로그래머스 레벨 5
    "Bronze": 3,  # 백준 브론즈
    "Silver": 2,  # 백준 실버
    "Gold": 1,  # 백준 골드
}

def generate_readme():
    content = HEADER

    # 문제 풀이를 저장할 딕셔너리
    problems = {
        "백준": {},
        "프로그래머스": {}
    }

    for root, dirs, files in os.walk("."):
        if root == ".":
            continue

        # 상위 디렉토리 이름 확인 (백준/프로그래머스 구분)
        parent_dir = os.path.basename(os.path.dirname(root))
        if parent_dir not in problems:
            continue

        # 단계별 디렉토리 이름 (예: Gold, Silver, 1, 0 등)
        stage = os.path.basename(root)

        if stage not in problems[parent_dir]:
            problems[parent_dir][stage] = {}

        # 파일 탐색
        for file in files:
            file_path = os.path.join(root, file)
            file_link = f"[{os.path.basename(file)}]({quote(file_path)})"

            # 문제 번호는 현재 디렉토리 이름
            problem_number = os.path.basename(os.path.dirname(root))

            # 문제 데이터 초기화
            if problem_number not in problems[parent_dir][stage]:
                problems[parent_dir][stage][problem_number] = {"languages": {}, "solution": None}

            # 해설 파일 처리
            if file.endswith(".md"):
                problems[parent_dir][stage][problem_number]["solution"] = file_link

            # 언어 파일 처리
            else:
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")  # 매핑되지 않은 파일은 "기타"
                problems[parent_dir][stage][problem_number]["languages"][language] = file_link

    # README.md 생성
    for category, stages in problems.items():
        content += f"## 📚 {category}\n"

        # 단계별 정렬: LEVEL_PRIORITY 값으로 내림차순 정렬
        sorted_stages = sorted(
            stages.items(),
            key=lambda x: LEVEL_PRIORITY.get(x[0], 100),  # 값이 없으면 마지막에 배치
            reverse=True  # 내림차순 정렬
        )

        for stage, problems in sorted_stages:
            if not problems:  # 저장된 문제가 없는 단계는 제외
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

    with open("README.md", "w") as fd:
        fd.write(content)
    print("README.md has been updated successfully.")


if __name__ == "__main__":
    generate_readme()
