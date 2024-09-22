def solution(myString):
    answer = ''
    
    for i in myString:
        answer += i > 'l' and i or 'l'
    
    return answer