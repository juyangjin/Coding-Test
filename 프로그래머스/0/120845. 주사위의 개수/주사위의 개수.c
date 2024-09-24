#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int box[], size_t box_len, int n) {
    int answer = 1;
    
    for(int i=0;i<box_len;i++){
        answer *= box[i]/n;
    }
    
    return answer;
}