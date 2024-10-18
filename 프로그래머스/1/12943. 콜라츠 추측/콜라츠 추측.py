def solution(num):
    answer = num
    
    for i in range(500):
        if answer == 1:
            return i;
        if answer % 2 == 0:
            answer /= 2
        else:
            answer = answer * 3 + 1
    
    return -1