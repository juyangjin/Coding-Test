#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(const char* strlist[], size_t strlist_len) {
    int* answer = (int*)malloc(strlist_len * sizeof(int));
    
    for(int i=0;i<strlist_len;i++){
        answer[i] = strlen(strlist[i]);
    }
    
    return answer;
}