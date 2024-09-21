def solution(hp):
    answer = 0
    q = hp // 5;
    s = hp % 5;
    answer =  hp % 5 != 0 and s % 3 != 0 and q + (s//3) + s % 3 or q + (s//3) or q;
        
    
    return answer
