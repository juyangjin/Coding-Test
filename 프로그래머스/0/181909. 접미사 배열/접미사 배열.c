#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void *p1, const void *p2) {
    return strcmp(*(char**)p1, *(char**)p2);
}

char** solution(const char* my_string) {
    char** answer = (char**)malloc(strlen(my_string) * sizeof(char*));
    
    for(int i = 0; i < strlen(my_string); i++)
        answer[i] = &my_string[i];
    qsort(answer, strlen(my_string), sizeof(char*), compare);
    
    return answer;
}