import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        
        List<Integer> honor = new ArrayList<>();
        
        for(int i=0;i<score.length;i++){
            honor.add(score[i]);
            
            if(honor.size() > k){
                honor.remove(Collections.min(honor));
            }
            
            answer[i] = Collections.min(honor);
        }
        
        return answer;
    }
}