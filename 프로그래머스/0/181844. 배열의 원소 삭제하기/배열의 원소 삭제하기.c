#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int* solution(int arr[], size_t arr_len, int delete_list[], size_t delete_list_len) {
    int i, j, len = 0;
    int* answer = (int*)malloc(arr_len * sizeof(int));
    for(i = 0; i<arr_len; i++){
        for(j = 0; j<delete_list_len; j++){
            if(arr[i] == delete_list[j]) break;
        }
        if(j == delete_list_len) answer[len++] = arr[i];
    }
    return answer;
}