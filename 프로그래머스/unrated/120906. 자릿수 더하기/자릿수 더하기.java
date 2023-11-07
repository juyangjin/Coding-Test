import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        String tp = Integer.toString(n);
        
        for(int i=0;i<tp.length();i++){
            answer += Integer.parseInt(tp.substring(i,i+1)); 
        }
        return answer;
    }
}