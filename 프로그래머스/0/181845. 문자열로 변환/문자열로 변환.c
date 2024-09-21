#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(int n) {
    char* answer = (char*)malloc(5 * sizeof(int));
    sprintf(answer, "%d", n);
    
    return answer;
}