def solution(n):
    answer = []
    
    for i in range(n+1):
        if i != 0 and n % i == 0:
            answer.append(i);
    
    return answer