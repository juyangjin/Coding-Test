#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* letter) {
    char* answer = (char*)malloc(strlen(my_string) + 1);
    int len = 0;
    
    for(int i = 0; i < strlen(my_string); i++){
        if(my_string[i] != letter[0])
            answer[i-len] = my_string[i];    
        else len++;

    }
     answer[strlen(my_string)-len] = '\0';
    return answer;
}