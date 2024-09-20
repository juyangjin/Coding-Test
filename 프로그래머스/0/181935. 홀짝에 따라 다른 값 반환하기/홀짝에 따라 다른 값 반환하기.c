#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    
    if(n % 2 == 0){
        for(int i=1;i<=n;i++){
            if(i % 2 == 0){
                answer += i * i;
            }
        }
    }
    
    else{
        for(int j=1;j<=n;j++){
            if(j % 2 != 0){
                answer += j;
            }
        }
    }
    
    return answer;
}