#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(const char* myString) {
    int* answer = (int*)malloc(strlen(myString) * sizeof(int));
    int len = 0;
    int cnt = 0;
    int end = strlen(myString)-1;
    
    for(int i=0;i<strlen(myString);i++){
        if(myString[i] == 'x'){
            answer[len++] = cnt;
            cnt = 0;
        }else{
            cnt++;
            if(i == end) answer[len++] = cnt;
        }
    }

    
    answer[len] = '\0';
    return answer;
} 