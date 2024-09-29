#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* number) {
    int answer = 0;
    
    for(int i=0;i<strlen(number);i++){
        answer += number[i] - '0';
    }
    
    answer %= 9;
    
    return answer;
}