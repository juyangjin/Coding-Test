class Solution {
    public int solution(int n) {
        int answer = 0;//0으로 초기화했기 때문에 맨 오른쪽 값 0부터 계산이 편하다.
        
        while(n > 0){
            answer = answer * 3 + (n % 3);
            n /= 3;
        }
        
        return answer;
    }
}
