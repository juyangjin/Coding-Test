#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int money) {
    int* answer = (int*)malloc(2);
    if(money%5500 == 0){
        answer[0] = money/5500;
        answer[1] = 0;
    }else{
        answer[0] = money/5500;
        answer[1] = money%5500;
    }
    
    return answer;
}