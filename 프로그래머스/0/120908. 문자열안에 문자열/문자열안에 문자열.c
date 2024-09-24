#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* str1, const char* str2) {
    if (strstr(str1,str2) != 0) return 1;
    return 2;
}