import java.util.Arrays;
    
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        int j = 0;
        int x = score.length / m; //상자 갯수
        int[] nscore = new int[score.length];
        Arrays.sort(score); //정렬
        
        for(int i=score.length-1; i>=0;i--) {
            nscore[j] += score[i]; //reverse
            j++;
        }
        
        System.out.println("");  
        for(int z=0;z < nscore.length;z+=m) {
            if(z==0) {
                z--; //제일 작은 숫자를 찾기 위해
            }else {
            answer += nscore[z] * m;
            }
        }
        
        return answer;
    }
}