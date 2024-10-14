def solution(board, k):
    answer = 0
    
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if i + j <= k :
                answer += board[i][j]
    
    return answer