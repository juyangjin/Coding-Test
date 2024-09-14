#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int count(int big){
    int cnt = 0;
    while(big !=0){
        big = big/10;
        cnt++;
    }
    return cnt;
}

int solution(int a, int b) {
    int answer = 0;
    int cnt = 0;
    int ab, ba = 0;
    int acnt = count(a);
    int bcnt = count(b);
    
    ab = (a * pow(10,bcnt)) + b;
    ba = (b * pow(10,acnt)) + a;
    
    answer = ab != ba ? ab > ba ? ab : ba : ab;
    
    return answer;
}