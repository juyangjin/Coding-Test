#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num, int k) {
    int answer = 0;
    int cnt = 1;
    
    while(num > 0){
        if(num % 10 != k){
            cnt++;       
        }else{
            answer = cnt;
        }
        num /= 10;
    }
    
    if(answer == 0) return -1;
    else return cnt - answer +1;
}