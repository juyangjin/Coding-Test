#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int n) {
    int len_str = strlen(my_string);
    char* answer = (char*)malloc(len_str * n);
    int len = 0;
    
    for(int i=0;i<len_str;i++){
        for(int j=0;j<n;j++){
            answer[len++] = my_string[i];
        }
    }
    
    answer[len] = '\0';
    return answer;
}