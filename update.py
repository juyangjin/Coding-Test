#!/usr/bin/env python

import os

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

EXISTING_CONTENT_PATH = "README.md"  # 수정할 README 파일 경로

# 문제를 난이도별로 나누기 위한 기준 (예시)
PROGRAMMERS_LEVELS = ["0단계", "1단계", "2단계", "3단계", "4단계"]
BAEKJOON_LEVELS = ["Bronze", "Silver", "Gold"]

def main():
    # 새로 생성될 내용
    content = HEADER

    # 문제 목록을 난이도별로 나누기 위한 딕셔너리
    programmers_problems = {level: [] for level in PROGRAMMERS_LEVELS}
    baekjoon_problems = {level: [] for level in BAEKJOON_LEVELS}

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

        # 문제 목록을 분류하기 위한 과정
        if directory == "프로그래머스":
            for file in files:
                # 프로그래머스의 문제는 단계별로 분류
                level = determine_programmers_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    programmers_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language
                    })

        elif directory == "백준":
            for file in files:
                # 백준 문제는 난이도별로 분류
                level = determine_baekjoon_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    baekjoon_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language
                    })

    # 백준 문제 목록 섹션 추가
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

    # 프로그래머스 문제 목록 섹션 추가
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

def determine_programmers_level(file_name):
    """프로그래머스 문제의 단계별 분류를 결정하는 함수"""
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

def determine_baekjoon_level(file_name):
    """백준 문제의 난이도별 분류를 결정하는 함수"""
    if "Bronze" in file_name:
        return "Bronze"
    elif "Silver" in file_name:
        return "Silver"
    elif "Gold" in file_name:
        return "Gold"
    return None

def determine_language(file_name):
    """파일 확장자에 따른 언어 결정"""
    if file_name.endswith(".py"):
        return "Python"
    elif file_name.endswith(".java"):
        return "Java"
    elif file_name.endswith(".cpp"):
        return "C++"
    elif file_name.endswith(".sql"):
        return "SQL"
    # 필요에 따라 다른 언어 추가 가능
    return "Unknown"

def get_file_extension(language):
    """언어에 맞는 파일 확장자를 반환"""
    if language == "Python":
        return ".py"
    elif language == "Java":
        return ".java"
    elif language == "C++":
        return ".cpp"
    elif language == "SQL":
        return ".sql"
    return ""

if __name__ == "__main__":
    main()
