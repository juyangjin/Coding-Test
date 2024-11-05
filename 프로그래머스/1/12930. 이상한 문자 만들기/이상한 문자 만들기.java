class Solution {
    public String solution(String s) {
        String[] ss = s.split("");
        String answer = "";
        int tmp = 0;
        
        for(int i=0;i<ss.length;i++){
            if(ss[i].equals(" ")){
                tmp = -1;
            }
            if(tmp % 2 == 0){
                answer += ss[i].toUpperCase();
            }else{
                answer += ss[i].toLowerCase();
            } 
            tmp++;
        }
        
        return answer;
    }
}