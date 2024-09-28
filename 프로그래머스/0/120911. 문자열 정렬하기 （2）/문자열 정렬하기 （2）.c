#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* compare(const int* a, const int* b){
    return strcmp((char *)a, (char *)b);
}

char* solution(const char* my_string) {
    char* answer = (char*)malloc(strlen(my_string) * sizeof(char));
    strcpy(answer, my_string);
    
    for(int i=0;i<strlen(my_string);i++){
        if(my_string[i] >= 'A' && my_string[i] <= 'Z'){
            answer[i] -= 'A' - 'a';
        }
    }
    
    qsort(answer, strlen(my_string), sizeof(char), compare);

    return answer;
}