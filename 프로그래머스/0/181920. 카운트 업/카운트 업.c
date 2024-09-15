#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int start_num, int end_num) {
    int* answer = (int*)malloc((end_num - start_num + 2) * sizeof(int));
    int len = 0;
    
    for(int i=start_num;i<=end_num;i++){
        answer[len++] = i;
    }
    answer[len] = '\0';
    return answer;
}