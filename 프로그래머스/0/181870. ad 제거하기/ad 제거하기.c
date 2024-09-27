#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* strArr[], size_t strArr_len) {
    char** answer = (char**)malloc(strArr_len * 20 * sizeof(char));
    int len = 0;
    
    for(int i=0;i<strArr_len;i++){
        answer[i] = (char*)malloc(20 * sizeof(char));
        if(strstr(strArr[i], "ad") == NULL) answer[len++] = strArr[i]; 
    }
    
    return answer;
}