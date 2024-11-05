import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] c = s.split("");
        Arrays.sort(c, Collections.reverseOrder());         
        
        for(String a : c){
            answer += a;
        }
    
        return answer;
    }
}