#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* compare(const int* a, const int* b){
    return (*a - *b);
}

int* solution(const char* my_string) {
    int* answer = (int*)malloc(strlen(my_string) * sizeof(int));
    int len = 0;
    
    for(int i=0;i<strlen(my_string);i++){
        if(isdigit(my_string[i])){
            answer[len++] = my_string[i] - '0';
        }
    }
    
    qsort(answer, len, sizeof(int), compare);
    
    return answer;
}