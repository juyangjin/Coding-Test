def solution(arr):
    answer = 0
    
    for i in arr:
        answer += i
        
    answer *= 1.0
    answer /= len(arr)
    
    return answer