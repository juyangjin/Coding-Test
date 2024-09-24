#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


char* solution(const char* myString) {
    char* answer = (char*)malloc(strlen(myString) * sizeof(char));  
    strcpy(answer, myString);
    
    for(int i=0;i<strlen(myString);i++){
        if(answer[i] >= 'A' && answer[i] <= 'Z'){
            answer[i] -= 'A' - 'a';
        }
        
    }
    
    return answer;
}