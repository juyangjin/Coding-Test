def solution(n):
    result = list((str(n)))
    result.sort()
    result.reverse();
    result = "".join(result) 
    
    return int(result)