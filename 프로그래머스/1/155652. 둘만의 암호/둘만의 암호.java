import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        Set<Character> skipSet = new HashSet<>();
        
        for(char c : skip.toCharArray()) {
            skipSet.add(c);
        }
        
        StringBuilder sb = new StringBuilder();
        
        for(char c : s.toCharArray()) {
            char next = c;
            int move = 0;
            while (move < index) {
                next++;
                if(next > 'z') next = 'a';
                if(skipSet.contains(next)) continue;
                
                move++;
            }
            sb.append(next);
        }
        return sb.toString();
    }
}