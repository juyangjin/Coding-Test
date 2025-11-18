class Solution {
    public int solution(int n) {

        // dp 배열: dp[i]는 i번째 피보나치 수를 의미
        // 문제에서 n은 최대 100,000까지 가능하므로 충분히 크게 배열 생성
        int[] dp = new int[n + 1];

        // 피보나치 기본값
        dp[0] = 0;
        dp[1] = 1;

        // 문제 요구: 모든 계산을 1234567로 나눈 나머지로 저장해야 함
        int MOD = 1234567;

        // 피보나치 점화식 적용: dp[i] = dp[i-1] + dp[i-2]
        // 단, 값이 너무 커지는 걸 방지하기 위해 매 연산마다 모듈러 적용
        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
        }

        // n번째 피보나치 수 반환
        return dp[n];
    }
}
