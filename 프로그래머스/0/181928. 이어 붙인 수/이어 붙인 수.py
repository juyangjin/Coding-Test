def solution(num_list):
    a = 0
    b = 0
    
    for i in num_list:
        if i % 2 == 1:
            a = a * 10 + i
        else:
            b = b * 10 + i
            
    return a + b