#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* str1, const char* str2) {
    char* answer = (char*)malloc(strlen(str1) + strlen(str2) * sizeof(char));
    int len = 0;
    
    for(int i=0;i<=strlen(str1);i++){
        answer[len++] = str1[i];
        answer[len++] = str2[i];
    }
    
    return answer;
}