import java.util.Arrays;

class Solution {
    public int[] solution(long n) {
        String c = String.valueOf(n);
        int[] answer = new int[c.length()];
        
        for(int i=0; i<answer.length;i++){
            answer[i] = Integer.parseInt(c.substring(answer.length-1-i,answer.length-i));
        }
        return answer;
    }
}