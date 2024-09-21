#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string, const char* is_prefix) {
    int answer = 1;
    
    for(int i=0;i<strlen(is_prefix);i++){
        if(my_string[i] != is_prefix[i]){
            answer = 0;
        }
    }
    
    return answer;
}