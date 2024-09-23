#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* my_string) {
    char** answer = (char**)malloc(sizeof(char*) * 500);
    char* tmp;
    int len = 0;
    
    tmp = strtok(my_string," ");
    
    while(tmp != NULL){
        answer[len++] = tmp;
        tmp = strtok(NULL," ");
    }
    
    return answer;
}