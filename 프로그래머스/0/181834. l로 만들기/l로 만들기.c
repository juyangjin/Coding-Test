#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* myString) {
    char* answer = (char*)malloc(strlen(myString));
    int i = 0;
 
    for(i=0;i<strlen(myString);i++){
        answer[i] = myString[i] > 'l' ? myString[i] : 'l';
    }
    
    answer[i] = '\0';
    return answer;
}