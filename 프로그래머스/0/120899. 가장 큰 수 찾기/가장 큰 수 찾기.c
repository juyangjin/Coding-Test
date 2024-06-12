#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int* solution(int array[], size_t array_len) {
    int* answer = (int*)malloc(2);
    answer[0] = 0;
    
    for(int i=0; i < array_len; i++){
        if(answer[0] < array[i]){
            answer[0] = array[i];
            answer[1] = i;
        }
    }
    return answer;
}