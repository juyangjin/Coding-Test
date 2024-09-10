#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// array_len은 배열 array의 길이입니다.
int solution(int array[], size_t array_len) {
    int answer,j,i,tmp = 0;
    
    for(int i=0; i<array_len; i++)
    {
        for(int j=0;j<array_len;j++)
            if(array[i]<array[j])
                {
                tmp=array[i];
                array[i]=array[j];
                array[j]=tmp;
            }
    }
    return answer = array[array_len/2];
}