class Solution {
    public int cnt(int a, int b){
        int tmp = 0;
        while(a > 0){
            if(a % 10 == b) tmp++;
            a /= 10;
        }
        return tmp;
    }
    
    public int solution(int i, int j, int k) {
        int answer = 0;
        
        for(int m=i; m<=j;m++){
            answer += cnt(m, k);
        }
        return answer;
    }
}