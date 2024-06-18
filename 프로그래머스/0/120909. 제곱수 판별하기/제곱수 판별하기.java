import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=0;i<n;i++){
            answer = Math.sqrt(n)%1 == 0 ? 1 : 2;
        }
        return answer;
    }
}