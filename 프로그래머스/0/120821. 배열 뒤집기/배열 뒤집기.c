#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len) {
    int* answer = (int*)malloc(num_list_len * sizeof(int));
    int len = 0;
    
    for(int i=num_list_len-1;i>=0;i--){
        answer[len++] = num_list[i];
    }
    
    return answer;
}