import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0;i<commands.length;i++){
            int len = 0;
            int f = commands[i][0] - 1;
            int e = commands[i][1] - 1;
            int n = commands[i][2] - 1;
            int[] tmp = new int[e-f+1];
            
            for(int j=f;j<=e;j++){
                tmp[len++] = array[j];
            }
            Arrays.sort(tmp);
            answer[i] = tmp[n];
        }        
        return answer;
    }
}