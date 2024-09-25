#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    int* answer = (int*)malloc(num_list_len * sizeof(int));
    
    for(int i=0;i<num_list_len;i++){
        answer[i] = num_list[(i+n) % num_list_len];
    }
    
    return answer;
}