#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int k) {
    int* answer = (int*)malloc(arr_len * sizeof(int));
    int len = 0;
    for(int i=0;i<arr_len;i++){
        if(k % 2 == 0) answer[i] = arr[i] + k;
        else answer[i] = arr[i] * k;
    }
    return answer;
}