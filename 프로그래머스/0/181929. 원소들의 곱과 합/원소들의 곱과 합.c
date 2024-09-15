#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num_list[], size_t num_list_len) {
    int x = 1;
    int p = 0;
    
    for(int i=0;i<num_list_len;i++){
        x *= num_list[i];
        p += num_list[i];
    }
    if(x < (p * p)) return 1;
    else return 0;
}