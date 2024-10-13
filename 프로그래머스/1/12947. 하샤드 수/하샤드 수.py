def solution(x):
    answer = True
    seat = sum(map(int, list(str(x))))
    if x % seat:
        answer = False
    return answer