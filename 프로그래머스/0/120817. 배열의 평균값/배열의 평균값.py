def solution(numbers):
    answer = 0
    
    for i in numbers:
        answer += i
    answer /= len(numbers)
    
    return answer