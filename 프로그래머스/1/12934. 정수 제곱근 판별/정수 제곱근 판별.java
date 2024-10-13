class Solution {
    public long squa(long a, long b){
        if(a * a == b) return (a+1) * (a+1);
        else return -1;
    }
    
    public long solution(long n) {
        long answer = -1;
        long tmp = 0;
        for(int i=0;i<=n;i++){
            tmp = squa(i,n);
            if(tmp != -1){
                return tmp;
            }
        }
        
        return answer;
    }
}