#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* str1, const char* str2) {
    int answer = 0;
    
    if(strstr(str2, str1) != 0) answer = 1;
    
    return answer;
}