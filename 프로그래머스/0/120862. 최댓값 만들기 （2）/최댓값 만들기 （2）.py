def solution(numbers):
    numbers.sort();
    t1 = numbers[0] * numbers[1]
    t2 = numbers[len(numbers)-1] * numbers[len(numbers)-2]
    
    if t1 > t2 :
        return t1
    else :
        return t2