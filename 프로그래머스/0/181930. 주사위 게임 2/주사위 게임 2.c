#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c) {
    int answer = a + b + c;
    
    if(a == b && b == c) answer *= ((a * a) + (b * b) + (c * c)) *  ((a * a * a) + (b * b * b) + (c * c * c));
    else if(a == b || b == c || a == c) answer *= ((a * a) + (b * b) + (c * c));
    
    return answer;
}