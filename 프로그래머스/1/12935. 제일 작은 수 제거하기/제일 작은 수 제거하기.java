class Solution {
    public int[] solution(int[] arr) {
        if(arr.length == 1){
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[arr.length-1];
        int min = arr[0];
        int len = 0;
        
      
        
        for(int i=0;i<arr.length;i++){
            min = Math.min(min, arr[i]);
        }
        
        for(int i=0;i<arr.length;i++){
            if(min != arr[i]){
                answer[len++] = arr[i];
            }
        }
            
       return answer;
    }
}