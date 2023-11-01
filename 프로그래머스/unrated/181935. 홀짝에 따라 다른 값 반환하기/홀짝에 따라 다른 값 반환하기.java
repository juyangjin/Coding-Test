class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if(n%2==1){
            answer = 1;
            for(int i=1;i<n;){
                i += 2;
                answer += i;
                }
            }
        else{
            for(int j=2;j<=n;){
                int temp = j;
                j += 2;
                int val = temp * temp;
                answer += val;
                 
            }
        }        
        return answer;
    }
}