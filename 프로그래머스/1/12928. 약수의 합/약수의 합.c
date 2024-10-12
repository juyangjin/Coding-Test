#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    
    for(int i=n;i>0;i--){
        answer += n % i == 0 ? i : 0;
    }
    
    return answer;
}