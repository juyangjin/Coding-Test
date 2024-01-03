import java.util.Arrays;

class Solution {
 public static int[] removeElement(int[] answer,int z){
     return Arrays.stream(answer)
                    .filter(i -> i != z)
                    .toArray();
 }
    
  public int[] solution(int n, int k) {
        int[] answer = new int[n+1];
      
        for(int i=0;i<=n;i++){
            answer[i] = i % k == 0 ? i : 0;
        }
        int z = 0;
            answer = removeElement(answer,z);
        
        return answer;
    }
}