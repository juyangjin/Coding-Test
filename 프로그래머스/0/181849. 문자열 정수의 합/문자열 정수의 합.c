#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* num_str) {
    int answer = 0;
    
    for(int i=0;i<strlen(num_str);i++){
        answer += num_str[i] - '0';
    }
    
    return answer;
}