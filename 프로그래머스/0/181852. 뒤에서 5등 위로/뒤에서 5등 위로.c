#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const int* a, const int* b){
    return (*a - *b);
}

int* solution(int num_list[], size_t num_list_len) {
    int* answer = (int*)malloc(num_list_len * sizeof(int));
    int len = 0;
    qsort(num_list ,num_list_len,sizeof(int),compare);
    
    for(int i=5;i<num_list_len;i++){
        answer[len++] = num_list[i];
    }
    
    answer[len] = '\0';
    return answer;
}