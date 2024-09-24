#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numbers[], size_t numbers_len, int num1, int num2) {
    int* answer = (int*)malloc(numbers_len);
    int len = 0;
    
    for(int i=num1;i<=num2;i++){
        answer[len++] = numbers[i];
    }
    
    return answer;
}