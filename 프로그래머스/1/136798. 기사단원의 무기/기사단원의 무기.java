class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for(int i=1;i<=number;i++){
            int result = 0;
            for(int j=1;j*j <=i;j++){
                if(i % j == 0){
                    result++;
                    if(j * j != i){
                        result++;
                    }
                }
            }
            if(result > limit){
                answer += power;
            }else{
                answer += result;
            }
        }
        return answer;
    }
}