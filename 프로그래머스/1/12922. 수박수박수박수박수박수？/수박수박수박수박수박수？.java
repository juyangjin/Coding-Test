class Solution {
    public String solution(int n) {
        String s = "수";
        String b = "박";
        String answer = "";
        
        for(int i=1;i<=n;i++){
            if(i%2 == 0){
                answer = answer.concat(b);
            }else{
                answer = answer.concat(s);
            }
        }
        return answer;
    }
}