#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int dot[], size_t dot_len) {
    int answer = 0;
    
    if(dot[0] != 0 && dot[1] != 0){
            if(dot[0] > 0 ){
                answer = dot[1] > 0 ? 1 : 4;
            }
            else{
                answer = dot[1] > 0 ? 2 : 3;
            }
        }
    
    return answer;
}