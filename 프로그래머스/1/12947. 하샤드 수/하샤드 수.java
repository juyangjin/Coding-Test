class Solution {
    public boolean ha(int a, int b){
        if(a % b == 0) return true;
        return false;
    }
    
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        int tmp = x;
        
        while(tmp > 0){
            sum += tmp % 10;
            tmp /= 10;
        }
        
        answer = ha(x,sum);
        
        return answer;
    }
}