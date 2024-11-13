import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, long left, long right) {
        int tmp = (int)right - (int)left +1;
        int[] answer = new int[tmp];
        int len = 0;

        for(long i=left;i<=right;i++){
            long a = i/n;
            long b = i%n;
            answer[len++] = Math.max((int)a,(int)b) + 1;
        }
        
        return answer;
    }
}