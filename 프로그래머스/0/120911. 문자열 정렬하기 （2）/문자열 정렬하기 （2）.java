import java.util.Arrays;

class Solution {  
    public String solution(String my_string) {
        String answer = "";
        my_string = my_string.toLowerCase();
        
        char[] list = my_string.toCharArray();
        Arrays.sort(list);
        
        answer = new String(list);
        
        return answer;
    }
}