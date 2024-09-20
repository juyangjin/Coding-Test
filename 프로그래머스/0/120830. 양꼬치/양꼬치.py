def solution(n, k):
    answer = 0
    
    if n > 9:
        answer = (n * 12000) + ((k-(n // 10)) * 2000)
    else:
        answer = (n * 12000) + (n * 2000)
    return answer