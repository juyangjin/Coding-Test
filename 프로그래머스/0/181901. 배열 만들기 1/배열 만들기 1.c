#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n, int k) {
    int* answer = (int*)malloc(n/k * sizeof(int));
    
    for(int i=0;i<n/k;i++){
        answer[i] = k * (i+1);
    }
    return answer;
}