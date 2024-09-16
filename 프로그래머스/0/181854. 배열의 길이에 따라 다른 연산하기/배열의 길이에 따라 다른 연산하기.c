#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int* solution(int arr[], size_t arr_len, int n) {
    int* answer = (int*)malloc(arr_len * sizeof(int));
    int j = arr_len % 2 == 0 ? n : 0;
    int h = arr_len % 2 == 0 ? 0 : n;
    
    for(int i=0;i<arr_len;i++){
        if(i % 2 == 0){
            answer[i] = arr[i] + h;
        }else{
            answer[i] = arr[i] + j;
        }
    }
    return answer;
}