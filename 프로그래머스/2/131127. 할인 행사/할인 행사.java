import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> needMap = new HashMap<>();
        int answer = 0;
        
        for(int i=0;i<number.length;i++) {
            needMap.put(want[i],number[i]);
        }
         
        for(int j=0;j<=discount.length-10;j++) {
            HashMap<String, Integer> countMap = new HashMap<>(needMap);
            for(int z=j;z<j+10;z++) {
                    if (countMap.containsKey(discount[z])) {
                        countMap.put(discount[z], countMap.get(discount[z]) - 1);
                    }
                }
            boolean allZero = true;
            for (Map.Entry<String,Integer> entry : countMap.entrySet()) {
                if (entry.getValue() != 0) {
                    allZero = false; 
                    break;
                } 
            }
            if (allZero) answer++;
            }       
        return answer;
    }
}