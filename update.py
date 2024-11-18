#!/usr/bin/env python

import os
from urllib import parse

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

EXISTING_CONTENT_PATH = "README.md"  # 기존 README.md 파일 경로
NEW_SECTION_HEADER = "## 📚 백준 문제 풀이 목록"  # 새로 추가할 섹션 제목

def main():
    # 기존 README 파일을 읽어 내용 유지
    if os.path.exists(EXISTING_CONTENT_PATH):
        with open(EXISTING_CONTENT_PATH, "r", encoding="utf-8") as f:
            existing_content = f.read()
    else:
        existing_content = ""  # 만약 README.md가 없다면 빈 문자열로 초기화

    content = existing_content  # 기존 내용을 그대로 가져옵니다.
    content += "\n\n"  # 기존 내용 뒤에 새로운 문제 목록을 추가

    content += HEADER

    directories = []
    solveds = []

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
        
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += f"## 📚 {directory}\n"
            else:
                content += f"### 🚀 {directory}\n"
                content += "| 문제번호 | 해설 | 언어 | 링크 |\n"
                content += "| ----- | ----- | ---- | ----- |\n"
            directories.append(directory)
        
        for file in files:
            # 문제 해설 페이지를 추가하는 방식으로 수정
            category_link = f"[해설](./{category}/{file.replace('.md', '')})"
            language = "md" if file.endswith(".md") else "Java"  # 예시로 Java와 md로 가정
            content += f"| {category} | {category_link} | {language} | [링크](./{category}/{file}) |\n"
            solveds.append(category)

    # 최종적으로 생성된 내용으로 README.md 파일을 덮어쓰기
    with open(EXISTING_CONTENT_PATH, "w", encoding="utf-8") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
