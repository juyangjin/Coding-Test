def solution(my_string):
    answer = []
    le = len(my_string)
    
    for i in range(le):
        answer.append(my_string[i:]);
    
    answer.sort()
    
    return answer