import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int Max_ = 0;
        int Min_ = 0;
  
        for(int i=0;i<sizes.length;i++){
            int Mx = Math.max(sizes[i][0], sizes[i][1]);
            int Mn = Math.min(sizes[i][0], sizes[i][1]);
            Max_ = Math.max(Max_, Mx);
            Min_ = Math.max(Min_, Mn);
           
        }
        return  Max_ * Min_;
    }
}