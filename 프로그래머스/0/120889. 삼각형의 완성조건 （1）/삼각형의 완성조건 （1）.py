def solution(sides):
    answer = 0
    
    sides.sort();
    answer = sides[0] + sides[1] > sides[2] and 1 or 2;
    
    return answer