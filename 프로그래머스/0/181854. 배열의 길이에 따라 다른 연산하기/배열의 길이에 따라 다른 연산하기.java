class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = new int[arr.length];
        int j = arr.length % 2 == 0 ? n : 0;
        int h = arr.length % 2 == 0 ? 0 : n;
        
        for(int i=0;i<arr.length;i++){
            if(i % 2 == 0){
                answer[i] = arr[i] + h;
            }else{
                answer[i] = arr[i] + j;
            }
        }
        
        return answer;
    }
}