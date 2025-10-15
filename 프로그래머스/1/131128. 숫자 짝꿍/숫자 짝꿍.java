import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        int[] countX = new int[10];
        int[] countY = new int[10];
        
        //문자열을 정수배열로 변환
        for(int c : X.toCharArray()) {
            countX[c - '0']++;
        }
        
        for (char c : Y.toCharArray()) {
            countY[c - '0']++;
        }
        
        StringBuilder sb = new StringBuilder();
        for(int i=9;i >= 0;i--){
            int num = Math.min(countX[i], countY[i]);
            for(int j=0;j < num;j++){
                sb.append(i);
            }
        }
        
        if (sb.length() == 0){
            answer = "-1";   // 공통 없음
        } else if (sb.charAt(0) == '0'){
            answer = "0"; // 전부 0 
        } else {
            answer = sb.toString();
        }
        
        return answer;
    }
}