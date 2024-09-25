#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numbers[], size_t numbers_len, const char* direction) {
    int* answer = (int*)malloc(numbers_len * sizeof(int));
    int i = 0;
    
    for(i=0;i<numbers_len;i++){
        if(strcmp(direction, "right") == 0){
            if(i==0) answer[0] = numbers[numbers_len-1];
            else answer[i] = numbers[i-1];
        }else{
            answer[i] = numbers[(i+1) % numbers_len];
        }
    }
    
    answer[i] = '\0';
    return answer;
}