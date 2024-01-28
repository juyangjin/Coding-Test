class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        int num = cipher.length() % code == 0 ? cipher.length() / code :
        (cipher.length()/code) - 1;
        
        for(int i=code-1;i<cipher.length();i+=code){
            answer += cipher.charAt(i);          
        }
        
        return answer;
    }
}