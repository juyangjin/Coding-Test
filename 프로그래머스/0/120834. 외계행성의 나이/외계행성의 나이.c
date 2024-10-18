#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int age) {
    char* answer = (char*)malloc(5 * sizeof(char*));
    char* str = "abcdefghij";
    int a = age;
    int cnt = -1;
    
    while(a > 0){
        a/= 10;
        cnt++;
    }
    
    for(int i=cnt;i>=0;i--){
        answer[i] = str[age%10];
        age /= 10;
    }
    
    return answer;
}