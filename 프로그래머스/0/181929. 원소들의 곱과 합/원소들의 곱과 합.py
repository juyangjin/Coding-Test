def solution(num_list):
    answer = 0;
    x = 1;
    p = 0;
    
    for i in num_list:
        x *= i;
        p += i;
    
    if x < (p * p) :        
        answer = 1;
        
    return answer