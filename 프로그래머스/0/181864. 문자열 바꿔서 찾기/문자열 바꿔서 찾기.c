#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* myString, const char* pat) {
    char tmp[strlen(myString)+1];
    
    for(int i=0;i<strlen(myString);i++){
        tmp[i] = myString[i] == 'A' ? 'B': 'A';
    }  
    return strstr(tmp, pat) ? 1 : 0;
}