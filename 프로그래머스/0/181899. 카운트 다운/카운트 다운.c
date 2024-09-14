#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start_num, int end_num) {
    int len = start_num - end_num + 1;
    int* answer = (int*)malloc(len * sizeof(int));
    
    for(int i=0;i<len;i++){
        answer[i] = start_num--;
    }
     return answer;
}