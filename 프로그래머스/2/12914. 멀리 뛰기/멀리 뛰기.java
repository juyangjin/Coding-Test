class Solution {
    public long solution(int n) {
        // dp[i] = i칸을 가는 방법의 수
        long[] dp = new long[n + 1];
        int MOD = 1234567;

        // 초기값 설정
        dp[0] = 1;   // 0칸 가는 방법: "아무 것도 안 함" 1가지로 보는게 편함
        dp[1] = 1;   // 1칸: (1)
        
        // n이 1일 수도 있으니, n이 1이면 바로 리턴
        if (n == 1) return dp[1];

        // 점화식: dp[i] = dp[i-1] + dp[i-2]
        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
        }

        return dp[n];
    }
}
