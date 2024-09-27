#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* my_string, int num1, int num2) {
    char* answer = (char*)malloc(strlen(my_string) * sizeof(char));
    strcpy(answer, my_string);
    
    answer[num1] = my_string[num2];
    answer[num2] = my_string[num1];
    
    return answer;
}