#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* rny_string) {
    char* answer = (char*)malloc(100 * sizeof(int));
    int len = 0;
    
    for(int i=0;i<strlen(rny_string);i++){
        if(rny_string[i] == 'm'){
            answer[len++] = 'r';
            answer[len++] = 'n';
        }else{
            answer[len++] = rny_string[i];
        }
    }
    
    answer[len] = '\0';
    return answer;
}