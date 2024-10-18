def solution(age):
    answer = ''
    alp = ['a','b','c','d','e','f','g','h','i','j']
    
    for i in str(age):
        answer += alp[int(i)]
    
    return answer