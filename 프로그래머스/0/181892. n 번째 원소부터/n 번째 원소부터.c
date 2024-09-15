#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    int* answer = (int*)malloc((num_list_len - n + 2) * sizeof(int));
    int len = 0;
    
    for(int i=n-1;i<num_list_len;i++){
        answer[len++] = num_list[i];
    }
    answer[len] = '\0';
    return answer;
}