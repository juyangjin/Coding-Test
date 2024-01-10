class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pcnt = 0;
        int ycnt = 0;
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == 'P' || s.charAt(i) == 'p'){
                pcnt++;
            }else if(s.charAt(i) == 'Y' || s.charAt(i) == 'y'){
                ycnt++;
            }
        }
        
        answer = pcnt == ycnt ? true : false;

        return answer;
    }
}