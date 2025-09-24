class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int temp = 0;
        
        for(int i=0;i<section.length;i++){
            if(m==1){
                answer++;
            }else if(i==0) {
                System.out.println("i번째 수는" + section[i]);
                temp = section[i] + m-1;
                answer++;
            }else if(temp < section[i]){
                    System.out.println("i번째 수는" + section[i]);
                    temp = section[i] + m-1;
                    answer++;
            }else{
                continue;
            }
            
        }
        
        return answer;
    }
}