#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* n_str) {
 char* answer = (char*)malloc(strlen(n_str));
    int len = 0;
    
    for(int i = 0; i < strlen(n_str);i++){
        if(n_str[i] != '0')
        {
            for(int j = i; j < strlen(n_str); j++)
                answer[len++] = n_str[j];
            break;
        }
    }
    answer[len] = '\0';
    return answer;
}