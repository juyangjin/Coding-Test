class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int [num_list.length];
        
        for(int i=1;i<=num_list.length;i++){
            answer[num_list.length-i] = num_list[i-1];
        }
        return answer;
    }
}