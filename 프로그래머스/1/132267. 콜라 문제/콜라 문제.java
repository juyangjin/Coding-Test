class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int tmp = 0;
        while(n >= a){
            if(n % a != 0) tmp += n % a;
            answer += (n / a) * b;
            n = (n / a) * b + (n % a);
        }

        
        return answer;
    }
}