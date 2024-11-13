class Solution {
    public int[] solution(int[] arr) {
        int arr_len = arr.length;
        int len = 1;
        
        while(len < arr_len){
            len *= 2;
        }
        
        int[] answer = new int[len];
        
        for(int i=0;i<arr.length;i++){
            answer[i] = arr[i];
        }
    
        return answer;
    }
}