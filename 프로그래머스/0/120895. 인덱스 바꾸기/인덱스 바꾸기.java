class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        StringBuilder b = new StringBuilder(my_string);
        b.setCharAt(num1, my_string.charAt(num2));
        b.setCharAt(num2, my_string.charAt(num1));
        
        answer = b.toString();
        
        return answer;
    }
}