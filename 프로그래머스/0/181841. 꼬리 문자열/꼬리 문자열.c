#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* str_list[], size_t str_list_len, const char* ex) {
    char* answer = (char*)malloc(str_list_len * sizeof(char) * 10);
    memset(answer, 0, sizeof(char) * str_list_len);
    
    for(int i=0;i<str_list_len;i++){
        if(strstr(str_list[i], ex) == NULL)
        {
            answer = strcat(answer, str_list[i]);
        }
    }
    
    return answer;
}