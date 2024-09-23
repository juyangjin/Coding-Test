#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int arr1[], size_t arr1_len, int arr2[], size_t arr2_len) {
    int answer = 0;
    int a = 0;
    int b = 0;
    
    if(arr1_len > arr2_len){
        answer = 1;
    }else if(arr1_len < arr2_len){
        answer = -1;
    }else{
        for(int i=0;i<arr1_len;i++){
            a += arr1[i];
            b += arr2[i];
        }
        answer = a == b ? 0 : a > b ? 1 : -1;
    }
    
    return answer;
}