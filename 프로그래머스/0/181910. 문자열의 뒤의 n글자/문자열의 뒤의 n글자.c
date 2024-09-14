#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int n) {
    int j = 0;
    char* answer = (char*)malloc(n * sizeof(int));
    
    for(int i = strlen(my_string) - n;i<strlen(my_string);i++){
        answer[j++] = my_string[i];
    }
    answer[j] = '\0';
    return answer;
}