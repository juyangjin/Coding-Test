import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer> runners = new HashMap<>();
        
        for (String r : participant){
            runners.put(r, runners.getOrDefault(r, 0) + 1);
        } //전체 참여자를 runner에 담고, value 값을 1씩 입력한다.
        
        for (String un : completion){
            runners.put(un, runners.get(un) - 1);
        } // 참여자 중에 completion에 해당하는 사람은 value값 -1
        
        for (String k : runners.keySet()) {
            if (runners.get(k) != 0) { 
                answer = k; //value가 0이 아닌 사람은 k에 추가한다.
                break;
            } 
        }
        return answer;
    }
}