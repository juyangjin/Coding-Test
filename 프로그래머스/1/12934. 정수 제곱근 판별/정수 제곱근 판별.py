def solution(n):
    squa = n ** (1/2)

    if squa % 1 == 0:
        return (squa + 1) ** 2
    return -1