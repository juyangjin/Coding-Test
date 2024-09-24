#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const int *a, const int *b){
    return (*a - *b);
}

int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    int i= numbers_len-1;
    
    qsort(numbers, numbers_len, sizeof(int), compare);
    
    answer = numbers[i] * numbers[i-1];
    
    return answer;
}