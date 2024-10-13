#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* binomial) {
    int answer = 0;
    int i = 0;
    int a = 0;
    int b = 0;
    while(binomial[i] != ' '){
        a = a * 10 + (binomial[i] - '0');
        i++;
    }
    i += 3;
    
    while(binomial[i] != '\0' || i < strlen(binomial)){
        b = b * 10 + (binomial[i] - '0');
        i++;
    }
    
    for(int i = 0; i<strlen(binomial); i++){
        if(binomial[i] == '+'){
            answer= a+b;
        }
        else if(binomial[i] == '-'){
            answer= a-b;
        }
        else if(binomial[i] == '*'){
            answer = a*b;
        }
    }
    
    return answer;
}