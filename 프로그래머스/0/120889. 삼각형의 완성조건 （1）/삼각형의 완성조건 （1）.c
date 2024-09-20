#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int m(const int* a, int* b){
    return (*a - *b);
}

int solution(int sides[], size_t sides_len) {
    int answer = 0;
    
    qsort(sides, sides_len, sizeof(int), m);  
    answer = sides[0] + sides[1] > sides[2] ? 1 : 2;
    
    return answer;
}