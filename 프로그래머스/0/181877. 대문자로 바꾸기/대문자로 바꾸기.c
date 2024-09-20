#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* myString) {
    char* answer = (char*)malloc(strlen(myString) + 1);
    strcpy(answer, myString);
    
    for(int i = 0; i < strlen(myString); i++) {
        if(answer[i] >= 'a' && answer[i] <= 'z'){
             answer[i] += 'A' - 'a';
        }
    } 
    return answer;
}