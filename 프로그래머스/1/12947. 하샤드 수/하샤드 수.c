#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    int a = x;
    int b = 0;
    
    while(a != 0){
        b += a%10;
        a /= 10;
    }
    
    if(x % b != 0) answer = false; 
    
    return answer;
}