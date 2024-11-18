import os
import subprocess
from urllib.parse import quote
import hashlib

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
    """Calculate the SHA256 hash of a file."""
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash


def generate_readme():
    content = HEADER
    repo_name = "Coding-Test"

    problems = {
        "백준": {},
        "프로그래머스": {}
    }

    for root, dirs, files in os.walk("."):
        if root == ".":
            continue

        parent_dir = os.path.basename(os.path.dirname(root))
        if parent_dir not in problems:
            continue

        stage = os.path.basename(root)

        if stage not in problems[parent_dir]:
            problems[parent_dir][stage] = {}

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            file_link = f"[{os.path.basename(file)}]({repo_name}/{quote(relative_path)})"

            problem_number = os.path.basename(os.path.dirname(root))

            if problem_number not in problems[parent_dir][stage]:
                problems[parent_dir][stage][problem_number] = {"languages": {}, "solution": None}

            if file.endswith(".md"):
                problems[parent_dir][stage][problem_number]["solution"] = file_link
            else:
                file_ext = os.path.splitext(file)[-1]
                language = LANGUAGE_MAP.get(file_ext, "기타")
                problems[parent_dir][stage][problem_number]["languages"][language] = file_link

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

    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as fd:
        fd.write(content)

    current_hash = calculate_file_hash(readme_path)

    if previous_hash == current_hash:
        print("No changes detected in README.md. Skipping commit and push.")
        return False

    print("README.md has been updated successfully.")
    return True


def commit_and_push():
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "Update README.md"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes have been pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")


if __name__ == "__main__":
    if generate_readme():
        commit_and_push()
