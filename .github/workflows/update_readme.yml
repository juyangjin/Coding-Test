#!/usr/bin/env python
import os
import subprocess
from urllib.parse import quote
import hashlib

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
이 저장소는 백준과 프로그래머스 문제 풀이를 정리한 저장소입니다.
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

def calculate_file_hash(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def generate_readme():
    print("Generating README...")
    content = HEADER
    problems = {}

    for root, dirs, files in os.walk("."):
        parent_dir = os.path.basename(os.path.dirname(root))
        if parent_dir not in ["백준", "프로그래머스"]:
            continue
        
        problem_number = os.path.basename(root)
        for file in files:
            file_ext = os.path.splitext(file)[-1].lower()
            language = LANGUAGE_MAP.get(file_ext, "기타")
            file_path = os.path.join(root, file)
            file_link = f"[{os.path.basename(file)}](/{quote(file_path)})"
            
            if problem_number not in problems:
                problems[problem_number] = {"languages": {}, "solution": None}
            
            if file.endswith(".md"):
                problems[problem_number]["solution"] = file_link
            else:
                problems[problem_number]["languages"][language] = file_link

    for problem, data in problems.items():
        solution = data["solution"] or "없음"
        languages = " / ".join(f"{lang}: {link}" for lang, link in data["languages"].items())
        content += f"| {problem} | {solution} | {languages} |\n"

    readme_path = "README.md"
    previous_hash = calculate_file_hash(readme_path)

    with open(readme_path, "w") as f:
        f.write(content)

    current_hash = calculate_file_hash(readme_path)

    return previous_hash != current_hash

def commit_and_push():
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "Update README.md"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

if __name__ == "__main__":
    if generate_readme():
        commit_and_push()
    else:
        print("No changes detected.")
