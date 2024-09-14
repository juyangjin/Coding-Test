#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* s1[], size_t s1_len, const char* s2[], size_t s2_len) {
    int answer = 0;
    
    for(int i=0;i<s1_len;i++){
        for(int j=0;j<s2_len;j++){
            if(strcmp(s1[i],s2[j]) == 0){
                answer++;
            }
        }
    }
    
    return answer;
}