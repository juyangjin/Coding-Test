class Solution {
    public int[] solution(int[] numbers, String direction) {
        int len = numbers.length;
        int[] answer = new int[len];
        
        for(int i=0;i<len;i++){
            if(direction.equals("right")){
                if(i == 0) answer[0] = numbers[len-1];
                else answer[i] = numbers[i-1];
            }
            else{
                answer[i] = numbers[(i+1) % len];
            }
        }      
        return answer;
    }
}