#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char** solution(const char* todo_list[], size_t todo_list_len, bool finished[], size_t finished_len) {
    char** answer = (char**)malloc(todo_list_len* todo_list_len* sizeof(char));
    int len = 0;
    
    for(int i=0;i<todo_list_len;i++){
        
        if(finished[i] == false) answer[len++] = todo_list[i];
    }
    
    return answer;
}