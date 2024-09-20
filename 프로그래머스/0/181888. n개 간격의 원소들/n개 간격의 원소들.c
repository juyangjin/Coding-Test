#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    int* answer = (int*)malloc(sizeof(num_list) * 20 * sizeof(int));
    int len = 0;
    
    for(int i=0;i<num_list_len;i++){
        if(i % n == 0){
           answer[len++] = num_list[i]; 
        } 
    }
    
    answer[len] = '\0';
    return answer;
}