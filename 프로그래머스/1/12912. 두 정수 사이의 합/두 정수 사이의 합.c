#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define min(x, y) (x) < (y) ? (x) : (y) 
#define max(x, y) (x) > (y) ? (x) : (y)

long long solution(int a, int b) {
    long long answer = 0;
    long long m = max(a,b);
    long long n = min(a,b);
    
    if(a == b){
        answer = a;
    }else{
        for(int i=n;i<=m;i++){
            answer += i;
        }
    }
    
    return answer;
}