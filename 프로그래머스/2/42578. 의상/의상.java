import java.util.*;
import java.util.Map.Entry;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap <String,Integer> set = new HashMap<>();
        
        for(String[] S : clothes){
            set.put(S[1], set.getOrDefault(S[1],0)+1);
        } // 배열에서 1번 값(의상 종류)을 겹치지 않게 정리
        
        for(Entry<String, Integer> entry : set.entrySet()) {
            answer *= entry.getValue()+1;
            System.out.println(answer);
        }//set의 전체값을 entry에 key, Value 형태로 저장 
        //answer값에 entry의 Value값(의상 종류 수) + 1을 곱한다.
        
        return answer-1;
    }
}