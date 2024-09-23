#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char** solution(const char* strArr[], size_t strArr_len) {
    char** answer = (char**)malloc(sizeof(char*) * strArr_len);
    
    for(int i=0;i<strArr_len;i++){
        size_t len = strlen(strArr[i]);
        char* temp = (char*)malloc(sizeof(char) * (len + 1));
        
        for (int j = 0; j < len; j++) {
            if (i % 2 == 0) {
                temp[j] = tolower(strArr[i][j]);
            } else {
                temp[j] = toupper(strArr[i][j]);
            }
            temp[len] = '\0';
            answer[i] = temp;
        }
    }
    return answer;
}