#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int solution(int n) {
    int answer = 0;
    for(int i=0;i<n;i++){
        if(i*i == n){
            return 1;
        }else if(i==n-1){
            return 2;
        }
    }
}