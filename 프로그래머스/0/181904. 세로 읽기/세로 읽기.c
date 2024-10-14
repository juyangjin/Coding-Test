#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int m, int c) {
    char* answer = (char*)malloc(strlen(my_string)+1);
    int len = 0;

    for(int i=c-1;i<strlen(my_string);i += m){
        answer[len++] = my_string[i];
    }
    
    answer[len] = '\0';
    return answer;
}