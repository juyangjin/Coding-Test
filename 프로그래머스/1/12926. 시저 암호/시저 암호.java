class Solution {
    public String solution(String s, int n) {
        String answer = "";
        
        for(int i=0;i<s.length();i++){
            int tmp = 0;
            if(s.charAt(i) != ' '){
                if(s.charAt(i) <= 90) {
                    tmp = s.charAt(i) + n;
                    if(tmp > 90) tmp -= 26;
                }else {
                    tmp = s.charAt(i) + n;
                    if(tmp > 122) tmp -= 26;
                }
                char t = (char) tmp;
                answer = answer.concat(String.valueOf(t));
            }else{
                answer = answer.concat(" ");
            }   
        }        
        return answer;
    }
}