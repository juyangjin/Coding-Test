#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long squa(long long a, long long b){
    if(a * a == b) return (a+1) * (a+1);
    else return -1;
}

long long solution(long long n) {
    long long answer = -1;
    
    for(int i=0;i<=n;i++){
        answer = squa(i,n);
        if(answer != -1){
            return answer;
        }
    }
    
    return answer;
}