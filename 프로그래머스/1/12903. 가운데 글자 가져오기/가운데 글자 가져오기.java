class Solution {
    public String solution(String s) {
        String answer = "";
        
        if(s.length() % 2 == 0){
            answer = answer.concat(String.valueOf(s.charAt((s.length()/2) -1)));
            answer = answer.concat(String.valueOf(s.charAt(s.length()/2)));
        }else{
            answer = answer.concat(String.valueOf(s.charAt(s.length()/2)));
        }
        
        return answer;
    }
}