#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int k) {
    char* answer = (char*)malloc(strlen(my_string) * k * sizeof(int));
    int len = 0;
    
    for(int i=0;i<k;i++){
        for(int j=0;j<strlen(my_string);j++){
            answer[len++] = my_string[j];
        }
    }
    
    answer[len] = '\0';
    return answer;
}