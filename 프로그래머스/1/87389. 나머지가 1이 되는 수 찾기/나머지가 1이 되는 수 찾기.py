def solution(n):
    return next(i for i in range(2, n) if n%i == 1)