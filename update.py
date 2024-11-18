#!/usr/bin/env python

import os
from urllib import parse
from collections import defaultdict

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

# 언어 확장자를 대응하는 딕셔너리
LANGUAGE_MAP = {
    "py": "Python",
    "java": "Java",
    "cpp": "C++",
    "js": "JavaScript",
    "c": "C",
    "rb": "Ruby",
    "go": "Go",
    "kt": "Kotlin",
    "swift": "Swift",
    "rs": "Rust",
}

def main():
    content = ""
    content += HEADER
    
    directories = set()
    problems = defaultdict(lambda: {"explanation": "", "files": []})  # 문제번호별로 그룹화
    difficulty_order = ['Bronze', 'Silver', 'Gold', 'Platinum', '백준', '프로그래머스']  # 난이도 순서

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
        
        # 문제별 카테고리 (예: Bronze, Silver) 처리
        if directory not in directories:
            if directory in difficulty_order:
                content += f"## 📚 {directory}\n"
                directories.add(directory)
        
        problem_id = os.path.basename(root)  # 문제번호 추출 (폴더 이름을 문제번호로 가정)
        problem_link = parse.quote(os.path.join(root, "README.md"))  # 문제해설 링크 (README.md로 가정)
        
        for file in files:
            # 파일 확장자 -> 언어로 변환
            file_extension = os.path.splitext(file)[1].lstrip('.')
            language = LANGUAGE_MAP.get(file_extension, file_extension)  # 언어 맵핑

            # 문제 파일 정보 추가
            problems[problem_id]["files"].append((language, os.path.join(root, file)))
            
            # 문제 해설 링크만 한 번만 추가
            if problems[problem_id]["explanation"] == "":
                problems[problem_id]["explanation"] = problem_link

    # 문제번호별로 출력 (기존 구조 유지)
    for problem_id, data in problems.items():
        explanation = data["explanation"]
        content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
        content += "| ----- | ----- | ---- | ----- |\n"
        
        # 문제번호, 해설 출력
        content += f"| {problem_id} | [해설]({explanation}) |"
        
        languages = []  # 언어별 풀이 파일 링크를 저장할 리스트
        for language, file_path in data["files"]:
            languages.append(f"[{language}]({parse.quote(file_path)})")
        
        # 각 언어별 파일 링크를 하나로 묶어서 출력
        content += " " + " | ".join(languages) + " |\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
