def solution(numLog):
    answer = ''
    tmp = 0
    
    for i in range(1,len(numLog)):
        tmp = int(numLog[i]) - int(numLog[i-1])
        if tmp == 1: answer += 'w'
        elif tmp == -1: answer +='s'
        elif tmp == 10: answer +='d'
        elif tmp == -10: answer += 'a'
        
    return answer