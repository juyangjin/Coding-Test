import os

HEADER = """#

"""

EXISTING_CONTENT_PATH = "README.md"  # 기존 README 파일
NEW_SECTION_HEADER = "## 📚 백준 문제 풀이 목록"  # 새로 추가할 섹션 제목

PROGRAMMERS_LEVELS = ["0단계", "1단계", "2단계", "3단계", "4단계"]
BAEKJOON_LEVELS = ["Bronze", "Silver", "Gold"]

def main():
    print("스캔 시작")
    # README.md 파일이 없다면 새로 생성
    if os.path.exists(EXISTING_CONTENT_PATH):
        print(f"기존 파일 {EXISTING_CONTENT_PATH} 읽기...")
        with open(EXISTING_CONTENT_PATH, "r", encoding="utf-8") as f:
            existing_content = f.read()
    else:
        print(f"기존 파일 {EXISTING_CONTENT_PATH}가 없으므로 새로 생성합니다.")
        existing_content = "# 백준, 프로그래머스 문제 풀이 목록\n\n"  # 기본 내용 추가

    content = existing_content  # 기존 내용을 그대로 가져옵니다.
    content += "\n\n"  # 기존 내용 뒤에 새로운 문제 목록을 추가

    content += HEADER  # 새로운 헤더 추가

    programmers_problems = {level: [] for level in PROGRAMMERS_LEVELS}
    baekjoon_problems = {level: [] for level in BAEKJOON_LEVELS}

    print("디렉토리 순회 시작")
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

        if directory == "프로그래머스":
            for file in files:
                level = determine_programmers_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    programmers_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language,
                        "file_name": file.replace('.md', '')  # 해당 문제 파일 이름
                    })

        elif directory == "백준":
            for file in files:
                level = determine_baekjoon_level(file)
                if level:
                    problem_link = f"[해설](./{category}/{file.replace('.md', '')})"
                    language = determine_language(file)
                    baekjoon_problems[level].append({
                        "problem": file.split(".")[0],
                        "link": problem_link,
                        "language": language,
                        "file_name": file.replace('.md', '')  # 해당 문제 파일 이름
                    })

    print("README 내용 추가 시작")
    content += "\n## 📚 백준 문제 풀이 목록\n"

    for level in BAEKJOON_LEVELS:
        if baekjoon_problems[level]:
            content += f"### 📚 백준 {level} 문제\n"
            content += f"<details>\n<summary>Click to expand</summary>\n"  # 접기 시작
            content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
            content += "| ----- | ----- | ---- | ----- |\n"
            for problem in baekjoon_problems[level]:
                file_extension = get_file_extension(problem['language'])
                language_link = f"[{problem['language']}](./{problem['file_name']}{file_extension})"
                content += f"| {problem['problem']} | {problem['link']} | {language_link} | [링크](./{problem['file_name']}{file_extension}) |\n"
            content += "</details>\n\n"  # 접기 끝

    content += "\n## 📚 프로그래머스 문제 풀이 목록\n"

    for level in PROGRAMMERS_LEVELS:
        if programmers_problems[level]:
            content += f"### 📚 프로그래머스 {level} 문제\n"
            content += f"<details>\n<summary>Click to expand</summary>\n"  # 접기 시작
            content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
            content += "| ----- | ----- | ---- | ----- |\n"
            for problem in programmers_problems[level]:
                file_extension = get_file_extension(problem['language'])
                language_link = f"[{problem['language']}](./{problem['file_name']}{file_extension})"
                content += f"| {problem['problem']} | {problem['link']} | {language_link} | [링크](./{problem['file_name']}{file_extension}) |\n"
            content += "</details>\n\n"  # 접기 끝

    print(f"최종 내용으로 {EXISTING_CONTENT_PATH} 파일을 덮어씁니다.")
    with open(EXISTING_CONTENT_PATH, "w", encoding="utf-8") as fd:
        fd.write(content)
    print(f"수정 완료: {EXISTING_CONTENT_PATH}")

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

def determine_baekjoon_level(file_name):
    if "Bronze" in file_name:
        return "Bronze"
    elif "Silver" in file_name:
        return "Silver"
    elif "Gold" in file_name:
        return "Gold"
    return None

def determine_language(file_name):
    if file_name.endswith(".py"):
        return "Python"
    elif file_name.endswith(".java"):
        return "Java"
    elif file_name.endswith(".cpp"):
        return "C++"
    elif file_name.endswith(".sql"):
        return "SQL"
    return "Unknown"

def get_file_extension(language):
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
