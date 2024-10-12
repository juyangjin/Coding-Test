def solution(a, b, c):
    answer = a + b + c
    
    if a == b and b == c:
        answer *= ((a * a) + (b * b) + (c * c)) *  ((a * a * a) + (b * b * b) + (c * c * c))
    elif a == b or b == c or a == c:
        answer *= ((a * a) + (b * b) + (c * c))
    
    return answer