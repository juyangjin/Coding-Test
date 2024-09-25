#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string) {
    char* answer = (char*)malloc(strlen(my_string) * sizeof(char));
    int len = 0;
    
    for(int i=0;i<strlen(my_string);i++){
        if(my_string[i] != 'a' && my_string[i] != 'e' && my_string[i] != 'i' && my_string[i] != 'o' && my_string[i] != 'u'){
            answer[len++] = my_string[i];
        }
    }
    
    answer[len] = '\0';
    return answer;
}