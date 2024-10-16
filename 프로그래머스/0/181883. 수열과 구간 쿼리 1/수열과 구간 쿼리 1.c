#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int** queries, size_t queries_rows, size_t queries_cols) {
    int* answer = (int*)malloc(arr_len * sizeof(int));
    
    for(int i=0;i<arr_len;i++){
        answer[i] = arr[i];
    }
    
    int len = 0;
    
    for(int i=0;i<queries_rows;i++){
        for(int j=queries[i][0];j<=queries[i][1];j++){
            answer[j] += 1;
        }        
    }
    
    return answer;
}