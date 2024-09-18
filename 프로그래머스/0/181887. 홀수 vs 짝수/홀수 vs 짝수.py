def solution(num_list):
    x = 0;
    y = 0;
    
    for i in range(0, len(num_list)):
        if i % 2 == 0:
            x += num_list[i];
        else:
            y += num_list[i];
            
    answer = x >= y and x or y;
    
    return answer