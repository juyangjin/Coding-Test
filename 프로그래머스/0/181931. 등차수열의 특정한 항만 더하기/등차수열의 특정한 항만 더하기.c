#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int d, bool included[], size_t included_len) {
          int answer = included[0] == true ? a : 0;
        int tmp = d;
        
        for(int i=1;i<included_len;i++){
            if(i == 1) d = a + d;
            if(included[i] == true){
                answer += d;
            }
            d += tmp;
        }
        
    return answer;
}