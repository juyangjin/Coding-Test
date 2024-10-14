def solution(n):
    answer = 0
    
    for i in range(4, n+1):
        tmp = 1
        for j in range(2, i+1):
            tmp += i % j == 0 and 1 or 0
    
        if tmp > 2 :
            answer += 1
    
    return answer