#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* rsp) {
    char* answer = (char*)malloc(100);
    int i = 0;
    
    for(i=0;i<strlen(rsp);i++){
        if(rsp[i] == '0') answer[i] = '5';
        else if(rsp[i] == '2') answer[i] = '0';
        else if(rsp[i] == '5') answer[i] = '2';
    }   
    
    answer[i] = '\0';
    return answer;
}