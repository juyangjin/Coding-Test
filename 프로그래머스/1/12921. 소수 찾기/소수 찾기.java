class Solution {
    public int solution(int n) {
        boolean[] isNotPrime = new boolean[n + 1];
        int answer = 0;
        
        for(int i = 2; i * i <= n;i++) {
            if(!isNotPrime[i]){
                //i의 배수는 전부 소수가 아님
                for (int j= i * i; j <= n; j += i) {
                    isNotPrime[j] = true;
                }
            }
        }
        
        // 2부터 n까지 소수가 아닌(false) 값만 세기
        for (int i = 2; i <= n; i++) {
            if (!isNotPrime[i]) {
                answer++;
            }
        }
        
        return answer;
    }
}