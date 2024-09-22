def num(i):
    return i % 2 == 1

def solution(a, b):
    answer = 0
    
    if num(a) and num(b): 
        answer = a * a + b * b
    elif num(a) or num(b):
        answer = 2 * (a + b)
    else:
        answer = a - b
        if answer < 0:
            answer *= -1;
    
    return answer