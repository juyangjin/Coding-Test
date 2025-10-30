import java.util.*;

class Solution {
    public String solution(String new_id) {
        Set<Character> rule = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        rule.add('-');
        rule.add('_');
        rule.add('.');
        
        for (char c = '0'; c <= '9'; c++) { rule.add(c); }
        for (char c = 'a'; c <= 'z'; c++) { rule.add(c); }
        
        new_id = new_id.toLowerCase();
        
          for (char ch : new_id.toCharArray()) {
            if (rule.contains(ch)) {
                sb.append(ch);
            }
        }
        String step3 = sb.toString().replaceAll("\\.{2,}", ".");
        
        String step4 = step3;
        if (step4.startsWith(".")) step4 = step4.substring(1);
        if (step4.endsWith(".")) step4 = step4.substring(0, step4.length() - 1);
    
        if (step4.isEmpty()) step4 = "a";
        
        if (step4.length() > 15) step4 = step4.substring(0, 15);
        if (step4.endsWith(".")) step4 = step4.substring(0, step4.length() - 1);
        
        while (step4.length() < 3) {
            step4 += step4.charAt(step4.length() - 1);
        }
        return step4;
    }
}