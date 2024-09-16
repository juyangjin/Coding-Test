#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len) {
    int* answer = (int*)malloc(arr_len * 100 * sizeof(int));
    int len = 0;
    
    for(int i=0;i<arr_len;i++){
        for(int j=0;j<arr[i];j++){
            answer[len++] = arr[i];
        }
    }
    
    answer[len] = '\0';
    return answer;
}