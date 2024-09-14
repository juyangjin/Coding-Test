#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    int answer = 0;
    int cnt = 0;
    int xx = 0;
    int xp = 0;
    int bb = b;
    
    while(bb!=0){
        bb=bb/10;
        cnt++;
    }
    
    xp = (a * pow(10, cnt)) + b;
    xx = 2 * a * b;
    answer = xx != xp ? xx < xp ? xp : xx : xp ;
    
    return answer;
    
}