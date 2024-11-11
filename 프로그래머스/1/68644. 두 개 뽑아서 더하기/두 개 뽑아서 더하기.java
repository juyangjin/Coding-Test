import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> arr = new ArrayList<Integer>();

        
        for(int i=0;i<numbers.length;i++){
            for(int j=i+1;j<numbers.length;j++){
               int tmp = numbers[i] + numbers[j];
                if(arr.indexOf(tmp) < 0){              
                    arr.add(tmp);  
                }                  
            }
        } 
        int[] answer = new int[arr.size()];    
        
        for(int i=0;i<arr.size();i++){
            answer[i] = arr.get(i);
        }
        Arrays.sort(answer);
        
        return answer;
    }
}