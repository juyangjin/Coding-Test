import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int cnt = 0;
        
        for(int i=0;i<arr.length;i++){
            cnt += arr[i] % divisor == 0 ? 1 : 0 ;
        }
        
        int[] answer = new int[cnt];
        if(cnt==0){
            int[] zero = {-1};
            return zero;
        }
        
        for(int i=0,j=0;i<arr.length;i++){
            if(arr[i]%divisor==0){
                answer[j] = arr[i];
                j++;
            }
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}