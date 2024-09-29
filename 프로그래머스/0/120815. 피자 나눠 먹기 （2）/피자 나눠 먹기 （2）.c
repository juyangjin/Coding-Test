#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    
    if(n % 6 == 0){
        answer = n / 6;
        return answer;
    }else{
        for(int i=n;i % 6 != 0;){
            i += n;
            if(i % 6 == 0) answer = i/6;
        }
    }
    
    
    return answer;
}