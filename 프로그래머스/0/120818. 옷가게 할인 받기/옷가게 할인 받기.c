#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int price) {
    return price >= 500000 ? price * 0.8f : price >= 300000 ? price * 0.9f : price >= 100000 ? price * 0.95f : price; 

}