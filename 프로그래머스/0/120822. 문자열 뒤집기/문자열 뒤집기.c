#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string) {
    char* answer = (char*)malloc(strlen(my_string) * sizeof(int));
    int len = 0;
    
    for(int i=strlen(my_string)-1;i>=0;i--){
        answer[len++] = my_string[i];
    }
    
    answer[len] = '\0';
    return answer;
}