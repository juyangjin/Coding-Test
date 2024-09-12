#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string) {
    int answer = 0;
    for(int i=0;i<strlen(my_string);i++){
        answer = my_string[i] > '0' && my_string[i] <= '9' ? answer + my_string[i] - '0' : answer;
    }
    return answer;
}