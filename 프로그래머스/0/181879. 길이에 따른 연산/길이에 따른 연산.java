class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        for(int i=0;i<num_list.length;i++){
            answer = num_list.length > 10 ? answer + num_list[i] : i==0 ? answer+1 * num_list[i]: answer * num_list[i];
        }
        return answer;
    }
}