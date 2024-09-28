#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int** intervals, size_t intervals_rows, size_t intervals_cols) {
    int* answer = (int*)malloc(arr_len * 2 * sizeof(int));
    int len = 0;
    
    for(int i=0;i<2;i++){
        for(int j=intervals[i][0];j<=intervals[i][1];j++){
            answer[len++] = arr[j];
        }
    }
    answer[len] = '\0';
    return answer;
}