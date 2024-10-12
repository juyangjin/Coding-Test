#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const int* a, const int* b){
    return (*a - *b);
}

int solution(int numbers[], size_t numbers_len) {
    qsort(numbers, numbers_len, sizeof(int), compare);
    int t1 = numbers[0] * numbers[1];
    int t2 = numbers[numbers_len-1] * numbers[numbers_len-2];
    
    if(t1 > t2) return t1;
    else return t2;   
}