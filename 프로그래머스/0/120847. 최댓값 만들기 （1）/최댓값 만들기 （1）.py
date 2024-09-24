def solution(numbers):
    answer = 0
    i = len(numbers)-1
    numbers.sort()
    answer = numbers[i] * numbers[i-1]

    return answer