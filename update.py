#!/usr/bin/env python

import os
from urllib import parse
from collections import defaultdict

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER
    
    directories = set()
    problems = defaultdict(lambda: {"explanation": "", "files": []})  # 문제번호별로 그룹화

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
        
        # 특정 카테고리만 처리 (백준, 프로그래머스 등)
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
            content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
            content += "| ----- | ----- | ---- | ----- |\n"
            directories.add(directory)

        for file in files:
            # 문제번호 및 풀이 파일 정보
            problem_id = os.path.basename(root)  # 문제번호 추출 (폴더 이름을 문제번호로 가정)
            problem_link = parse.quote(os.path.join(root, "README.md"))  # 문제해설 링크 (README.md로 가정)
            file_extension = os.path.splitext(file)[1].lstrip('.')  # 확장자 -> 언어로 간주 (예: .cpp -> C++)

            if category not in problems[problem_id]["files"]:
                problems[problem_id]["files"].append((file, file_extension, os.path.join(root, file)))
            
            # 문제 해설 링크만 한 번만 추가
            if problems[problem_id]["explanation"] == "":
                problems[problem_id]["explanation"] = problem_link

    # 문제번호별로 정렬하여 출력
    for problem_id, data in problems.items():
        explanation = data["explanation"]
        if explanation:
            content += "| {} | [해설]({}) |".format(problem_id, explanation)
        
        languages = []  # 언어별 풀이 파일 링크를 저장할 리스트
        for file, language, file_path in data["files"]:
            languages.append(f"[{language}]({parse.quote(file_path)})")
        
        # 각 언어별 파일 링크를 하나로 묶어서 출력
        content += " " + " | ".join(languages) + " |\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
