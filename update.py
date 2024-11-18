#!/usr/bin/env python

import os
from urllib import parse

# 기존 README 파일 경로
EXISTING_CONTENT_PATH = "README.md"  # 기존 README 파일
NEW_SECTION_HEADER = "## 📚 백준 문제 풀이 목록"  # 새로 추가할 섹션 제목

# 문제를 난이도별로 나누기 위한 기준
PROGRAMMERS_LEVELS = ["0단계", "1단계", "2단계", "3단계", "4단계"]
BAEKJOON_LEVELS = ["Bronze", "Silver", "Gold"]

# 기존 README.md 파일을 읽고, 새로운 문제 목록을 추가하는 함수
def main():
    # 기존 README 파일을 읽어 내용 유지
    if os.path.exists(EXISTING_CONTENT_PATH):
        with open(EXISTING_CONTENT_PATH, "r", encoding="utf-8") as f:
            existing_content = f.read()
    else:
        existing_content = ""  # 파일이 없다면 빈 문자열로 초기화

    # 기존 내용을 그대로 가져오고 새로운 문제 목록을 추가할 준비
    content = existing_content  # 기존 내용을 그대로 가져옵니다.
    content += "\n\n"  # 기존 내용 뒤에 새로운 문제 목록을 추가

    # 문제 목록을 난이도별로 나누기 위한 딕셔너리
    programmers_problems = {level: [] for level in PROGRAMMERS_LEVELS}
    baekjoon_problems = {level: [] for level in BAEKJOON_LEVELS}

    # 문제 파일을 순회하여 적절한 목록에 추가
    directories = []
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        if category == 'images':
            continue

        directory = os.path.basename(os.path.dirname(root))

        if directory == '.':
            continue

        # 프로그래머스 문제 처리
        if directory == "프로그래머스":
            for file in files:
                level = determine_programmers_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    programmers_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language
                    })

        # 백준 문제 처리
        elif directory == "백준":
            for file in files:
                level = determine_baekjoon_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    baekjoon_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language
                    })

    # README.md 내용에 백준 문제 목록 추가
    content += "\n## 📚 백준 문제 풀이 목록\n"

    # 백준 문제 난이도별 목록 추가
    for level in BAEKJOON_LEVELS:
        if baekjoon_problems[level]:
            content += f"### 📚 백준 {level} 문제\n"
            content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
            content += "| ----- | ----- | ---- | ----- |\n"
            for problem in baekjoon_problems[level]:
                file_extension = get_file_extension(problem['language'])
                content += f"| {problem['problem']} | {problem['link']} | {problem['language']} | [링크](./{problem['problem']}{file_extension}) |\n"
            content += "\n"

    # 프로그래머스 문제 목록 추가
    content += "\n## 📚 프로그래머스 문제 풀이 목록\n"

    # 프로그래머스 문제 난이도별 목록 추가
    for level in PROGRAMMERS_LEVELS:
        if programmers_problems[level]:
            content += f"### 📚 프로그래머스 {level} 문제\n"
            content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
            content += "| ----- | ----- | ---- | ----- |\n"
            for problem in programmers_problems[level]:
                file_extension = get_file_extension(problem['language'])
                content += f"| {problem['problem']} | {problem['link']} | {problem['language']} | [링크](./{problem['problem']}{file_extension}) |\n"
            content += "\n"

    # 최종적으로 생성된 내용으로 README.md 파일을 덮어쓰기
    with open(EXISTING_CONTENT_PATH, "w", encoding="utf-8") as fd:
        fd.write(content)

# 프로그래머스 문제의 단계별 분류를 결정하는 함수
def determine_programmers_level(file_name):
    if "0단계" in file_name:
        return "0단계"
    elif "1단계" in file_name:
        return "1단계"
    elif "2단계" in file_name:
        return "2단계"
    elif "3단계" in file_name:
        return "3단계"
    elif "4단계" in file_name:
        return "4단계"
    return None

# 백준 문제의 난이도별 분류를 결정하는 함수
def determine_baekjoon_level(file_name):
    if "Bronze" in file_name:
        return "Bronze"
    elif "Silver" in file_name:
        return "Silver"
    elif "Gold" in file_name:
        return "Gold"
    return None

# 파일 확장자에 따른 언어 결정
def determine_language(file_name):
    if file_name.endswith(".py"):
        return "Python"
    elif file_name.endswith(".java"):
        return "Java"
    elif file_name.endswith(".cpp"):
        return "C++"
    return "Unknown"

# 언어에 맞는 파일 확장자를 반환
def get_file_extension(language):
    if language == "Python":
        return ".py"
    elif language == "Java":
        return ".java"
    elif language == "C++":
        return ".cpp"
    return ""

if __name__ == "__main__":
    main()
