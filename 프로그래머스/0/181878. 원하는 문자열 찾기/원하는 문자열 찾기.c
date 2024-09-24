#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* myString, const char* pat) {
    int answer = 0;
    char* m = (char*)malloc(strlen(myString) + 1);
    char* p = (char*)malloc(strlen(pat)+1);
    strcpy(m, myString);
    strcpy(p, pat);
    
    for(int i=0;i<strlen(myString);i++){
        if(m[i] >= 'A' && m[i] <= 'Z') m[i] -= 'A' - 'a';
    }
    
    for(int i=0;i<strlen(pat);i++){
        if(p[i] >= 'A' && p[i] <= 'Z') p[i] -= 'A' - 'a';
    }
    
    if(strstr(m, p) != 0) answer = 1;
    
    return answer;
}