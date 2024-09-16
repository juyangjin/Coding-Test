#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string, const char* target) {
    const char* answer = strstr(my_string, target);    
    if(answer != 0) answer = 1;
    
    return answer;
}