import java.util.*;

class Solution {
    public boolean eq(int[] a, int b){
        for(int j : a){
            if(j == b) 
                return true;     
        } return false;  
    }
    
    public int[] solution(int[] arr, int[] delete_list) {     
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i: arr){
            if(!eq(delete_list, i)){
                list.add(i);
            }       
        }
        
        int[] answer = new int[list.size()];
        int len = 0;
        
        for(int j: list){
            answer[len++] = j;
        }   
        return answer;
    }
    
}
