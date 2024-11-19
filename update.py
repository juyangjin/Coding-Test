def generate_readme():
    """
    프로젝트 디렉토리 구조를 읽고 README.md 파일을 생성합니다.
    - 백준과 프로그래머스 문제를 분류하여 표로 출력합니다.
    """
    print("Starting README generation...")
    content = HEADER  # README 상단 헤더
    repo_name = "Coding-Test"  # GitHub 저장소 이름

    # 문제 저장 구조
    problems = {
        "백준": {},
        "프로그래머스": {},
    }

    # 디렉토리 탐색
    for root, dirs, files in os.walk("."):
        if root == ".":  # 최상위 디렉토리 무시
            continue

        parent_dir = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 이름 (백준/프로그래머스)
        if parent_dir not in problems:
            continue

        # 난이도 또는 레벨
        level = os.path.basename(root)

        if level not in problems[parent_dir]:
            problems[parent_dir][level] = {}

        # 현재 디렉토리 내 파일 처리
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_link = f"[{os.path.basename(file)}]({quote(relative_path)})"

            # 문제 번호 및 이름 추출
            problem_dir = os.path.basename(root)
            if "." in problem_dir:
                problem_number, problem_name = problem_dir.split(".", 1)
            else:
                problem_number = problem_dir
                problem_name = "Unknown"

            if problem_number not in problems[parent_dir][level]:
                problems[parent_dir][level][problem_number] = {
                    "name": problem_name.strip(),
                    "languages": {},
                    "solution": None,
                }

            # Markdown 파일은 해설로 처리
            if file.endswith(".md"):
                problems[parent_dir][level][problem_number]["solution"] = file_link
            else:
                # 확장자로 언어 감지
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")
                problems[parent_dir][level][problem_number]["languages"][language] = file_link

    # README 본문 생성
    for category, levels in problems.items():
        content += f"## 📚 {category}\n"

        for level, problems_in_level in sorted(levels.items(), key=lambda x: LEVEL_PRIORITY.get(x[0], 100), reverse=True):
            if not problems_in_level:  # 문제가 없으면 스킵
                continue

            content += f"### 🚀 {level}\n"
            content += "| 문제번호 | 문제 이름 | 해설 | 언어 |\n"
            content += "| -------- | --------- | ---- | ---- |\n"

            for problem_number, data in sorted(problems_in_level.items()):
                solution_link = data["solution"] if data["solution"] else "없음"
                language_links = " / ".join(
                    f"[{lang}]({link})" for lang, link in data["languages"].items()
                )
                if not language_links:
                    language_links = "없음"

                content += f"| {problem_number} | {data['name']} | {solution_link} | {language_links} |\n"

    # README 저장
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as fd:
        fd.write(content)

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:
        print("No changes detected in README.md.")
        return False

    print("README.md updated successfully.")
    return True
