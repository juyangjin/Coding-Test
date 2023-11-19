import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        String evens = "";
        String odds = "";
        int resurt = 0;
        
        for(int i=0;i<num_list.length;i++){
            if(num_list[i] % 2 == 0){
               evens += Integer.toString(num_list[i]);
            }
            else{
                odds += Integer.toString(num_list[i]);
            }
        }
        resurt = Integer.parseInt(evens) + Integer.parseInt(odds);
        return resurt;
    }
}