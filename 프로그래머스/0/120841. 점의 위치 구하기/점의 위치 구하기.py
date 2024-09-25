def solution(dot):
    answer = 0
    
    if dot[0] != 0 and dot[1] != 0:
            if dot[0] > 0:
                answer = dot[1] > 0 and 1 or 4
            else:
                answer = dot[1] > 0 and 2 or 3
                
    return answer