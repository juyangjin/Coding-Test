class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for(int i=0;i<my_string.length();i++){
            char item = my_string.charAt(i);
            if(Character.isUpperCase(item)){
                answer += Character.toLowerCase(item);
            }else{
                answer += Character.toUpperCase(item);
            }
        } 
        return answer;
    }
}