def solution(my_string):
    tmp = ("a,e,i,o,u")
    
    for i in tmp:
        my_string = my_string.replace(i,"")
    
    return my_string