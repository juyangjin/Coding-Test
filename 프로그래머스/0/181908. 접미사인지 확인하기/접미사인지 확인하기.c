#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int solution(const char* my_string, const char* is_suffix) {
    int a = strlen(my_string);
    int b = strlen(is_suffix);
    
    if(strcmp(my_string+a-b,is_suffix)==0) return 1;
    return 0;
}