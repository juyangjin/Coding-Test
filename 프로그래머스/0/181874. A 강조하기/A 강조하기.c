#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    char* answer = (char*)malloc(100);
    strcpy(answer, myString);
    int j = 0;
    
    for(int i=0;i<strlen(myString);i++){
        if(myString[i] == 'a' || myString[i] == 'A')
            answer[j++] = toupper('a');
        else
            answer[j++] = tolower(myString[i]);
    }
    
    return answer;
}