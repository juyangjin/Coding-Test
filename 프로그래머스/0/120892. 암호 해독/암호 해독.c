#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* cipher, int code) {
    char* answer = (char*)malloc(strlen(cipher)+1/code);

    int len = 0;
    
    for(int i=code;i<=strlen(cipher);i+=code){
        answer[len++] = cipher[i-1];
        }
    
    answer[len] = NULL;
    return answer;
}