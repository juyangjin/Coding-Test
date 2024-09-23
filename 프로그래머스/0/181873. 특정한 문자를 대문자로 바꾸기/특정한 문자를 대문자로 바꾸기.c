#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, const char* alp) {
    char* answer = (char*)malloc(strlen(my_string) * sizeof(int));
    
    strcpy(answer, my_string);
    
    for(int i=0;i<strlen(my_string);i++){
        if(answer[i] == *alp){
            answer[i] = toupper(*alp);
        }
    }
    
    return answer;
}