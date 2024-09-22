#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


char** solution(const char* names[], size_t names_len) {
    char** answer = (char**)malloc(names_len * sizeof(int));
    int len = 0;
    
    for(int i=0;i<names_len;i += 5){
        answer[len++] = names[i];
    }
    
    answer[len] = '\0';
    return answer;
}