#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int numLog[], size_t numLog_len) {
    char* answer = (char*)malloc(numLog_len+1 * sizeof(int));
    int tmp = 0;
    int len = 0;
    
    for(int i=1;i<numLog_len;i++){
        tmp = numLog[i] - numLog[i-1];
        if(tmp == 1) answer[len] = 'w';
        else if(tmp == -1) answer[len] = 's';
        else if(tmp == 10) answer[len] = 'd';
        else if(tmp == -10) answer[len] = 'a';
        len++;
    }
    
    answer[len] = '\0';
    return answer;
}