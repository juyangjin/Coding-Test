class Solution {
    public String solution(int[] food) {
        String answer = "";
        String reverse = "";
        for(int i=1;i<food.length;i++){
            int len = food[i]/2;
            for(int j=0;j<len;j++){
               answer = answer.concat(Integer.toString(i));  
            }   
        }
        
        for(int i=answer.length()-1;i>=0;i--){
            reverse += answer.charAt(i);
        }
        
        answer = answer.concat("0" + reverse);
        return answer;
    }
}