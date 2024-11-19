import os
from urllib import parse

# README 헤더 템플릿
HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

# 백준 난이도
BOJ_DIFFICULTY = {
    "Bronze": "브론즈",
    "Silver": "실버",
    "Gold": "골드",
    "Platinum": "플래티넘",
    "Ruby": "루비",
}

# 프로그래머스 난이도
PROGRAMMERS_DIFFICULTY = {
    "0": "level 0",
    "1": "level 1",
    "2": "level 2",
    "3": "level 3",
    "4": "level 4",
    "5": "level 5",
}

def extract_difficulty(category, directory_name):
    """디렉토리 이름에서 난이도를 추출하여 반환."""
    if category == "백준":
        for difficulty in BOJ_DIFFICULTY.keys():
            if difficulty.lower() in directory_name.lower():
                return BOJ_DIFFICULTY[difficulty]
    elif category == "프로그래머스":
        for level in PROGRAMMERS_DIFFICULTY.keys():
            if f"level{level}" in directory_name.lower():
                return PROGRAMMERS_DIFFICULTY[level]
    return "난이도 없음"  # 난이도 정보가 없으면 '난이도 없음' 표시

def main():
    content = HEADER
    directories = []  # 각 카테고리별 문제 리스트
    solveds = []  # 이미 처리한 문제 목록

    # 디렉토리 순회
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):  # 제외할 디렉토리
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        # 디렉토리 이름에서 카테고리 추출
        category = os.path.basename(root)

        # 'images' 디렉토리는 무시
        if category == 'images':
            continue

        # 상위 디렉토리 이름을 추출
        directory = os.path.basename(os.path.dirname(root))
        if directory == '.':
            continue

        # 카테고리별 섹션 추가
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += f"## 📚 {directory}\n"
                content += "| 난이도 | 문제번호 | 링크 |\n"
                content += "| ------ | --------- | ----- |\n"
            else:
                content += f"### 🚀 {directory}\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        # 문제 파일 처리
        for file in files:
            if category not in solveds:
                # 문제 디렉토리에서 난이도 추출
                difficulty = extract_difficulty(directory, root)

                # 문제 번호와 링크 추가
                content += f"| {difficulty} | {category} | [링크]({parse.quote(os.path.join(root, file))}) |\n"
                solveds.append(category)

    # README.md 파일 작성
    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
