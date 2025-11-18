class Solution {
    // 최대공약수 (유클리드 호제법)
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // 최소공배수
    private int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
    
    public int solution(int[] arr) {
        // 첫 번째 숫자를 기준으로 최소공배수를 누적 계산한다.
        int answer = arr[0];
        
        // arr[1]부터 차례대로 최소공배수 누적
        for (int i = 1; i < arr.length; i++) {
            answer = lcm(answer, arr[i]); 
        }
        
        return answer;
    }
}
