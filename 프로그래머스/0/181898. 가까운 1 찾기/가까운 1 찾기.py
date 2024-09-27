def solution(arr, idx):

    for i in range(idx,len(arr)):
        if arr[i] == 1:
            return idx
        else :
            idx += 1

    return -1