def generate_readme():
    """
    디렉토리 및 파일을 탐색하여 README.md를 생성합니다.
    """
    content = HEADER
    solved_problems = []  # 이미 처리된 문제 목록
    problems_by_category = {
        "백준": {difficulty: [] for difficulty in BOJ_DIFFICULTY_ORDER},
        "프로그래머스": {level: [] for level in PROGRAMMERS_DIFFICULTY_ORDER},
    }

    for root, dirs, files in os.walk("."):
        dirs.sort()  # 디렉토리 정렬
        if root == ".":
            # 최상위 디렉토리에서 제외할 디렉토리
            for exclude in (".git", ".github"):
                if exclude in dirs:
                    dirs.remove(exclude)
            continue

        category = os.path.basename(os.path.dirname(root))  # 상위 디렉토리 이름
        problem_dir = os.path.basename(root)  # 현재 디렉토리 이름
        problem_number, problem_name = split_problem_name(problem_dir)  # 문제 번호와 문제 이름 분리

        # 난이도 추출
        difficulty = extract_difficulty(problem_dir, category)

        # 난이도가 사전 정의된 범위 내에만 포함되도록 확인
        if category == "백준" and difficulty in BOJ_DIFFICULTY_ORDER:
            problems_by_category["백준"][difficulty].append((problem_number, problem_name, files, root))
        elif category == "프로그래머스" and difficulty in PROGRAMMERS_DIFFICULTY_ORDER:
            problems_by_category["프로그래머스"][difficulty].append((problem_number, problem_name, files, root))

    # 백준 및 프로그래머스 섹션 생성
    for category, difficulties in problems_by_category.items():
        content += f"## 📚 {category}\n"
        for difficulty, problems in difficulties.items():
            content += f"### 🚀 {difficulty}\n"
            content += "| 문제번호 | 문제 이름 | 언어 |\n"
            content += "| -------- | --------- | ----- |\n"

            if problems:
                for problem_number, problem_name, files, root in problems:
                    language_links = []
                    for file in files:
                        if file == "README.md":
                            continue
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, start=".")
                        file_ext = os.path.splitext(file)[-1].lower()
                        language = LANGUAGE_MAP.get(file_ext, "기타")
                        language_links.append(f"[{language}]({quote(relative_path)})")
                    
                    if language_links:
                        language_links.sort()
                        language_text = " / ".join(language_links)
                        content += f"| {problem_number} | {problem_name} | {language_text} |\n"
            else:
                content += "| 데이터가 없습니다 | | |\n"  # 데이터가 없을 때 표시

    # README 파일 작성
    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)
    if not os.path.exists(readme_path):
        print(f"{readme_path} not found. Creating new README file...")
    with open(readme_path, "w") as f:
        f.write(content)

    current_hash = calculate_file_hash(readme_path)
    if previous_hash == current_hash:
        print("No changes detected in README.md. Skipping commit and push.")
        return False
    print("README.md has been updated successfully.")
    return True
