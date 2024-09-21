#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num_list[], size_t num_list_len) {
    int a = 0;
    int b = 0;
    
    for(int i=0;i<num_list_len;i++){
        if(num_list[i] % 2) a = a * 10 + num_list[i];
        else b = b * 10 + num_list[i];
    } 
    return a + b;
}