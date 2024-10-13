def solution(a, b):
    answer = 0
    m = max(a,b)
    n = min(a,b)
    
    for i in range(n,m+1):
        answer += i;
    
    return answer