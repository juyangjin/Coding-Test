#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int angle) {
    int answer = angle == 180 ? 4 : angle > 90 && angle < 180 ? 3 : angle == 90 ? 2 : 1 ;
    return answer;
}