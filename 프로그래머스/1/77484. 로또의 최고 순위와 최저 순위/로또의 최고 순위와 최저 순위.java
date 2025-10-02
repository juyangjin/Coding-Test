class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int rank[] = {6,6,5,4,3,2,1};
        int zero = 0;
        int win_num = 0;
        
        for(int i=0;i<lottos.length;i++){
            if(lottos[i] == 0) {
                zero++;
            }else {
                for(int j=0;j<win_nums.length;j++){
                    if(lottos[i] == win_nums[j]){
                       win_num++; 
                    }
                }
            }    
        }
        
        int max = zero + win_num; 
        int min = win_num;

        
        answer[0] = rank[max]; 
        answer[1] = rank[min];
        
        return answer;
    }
}