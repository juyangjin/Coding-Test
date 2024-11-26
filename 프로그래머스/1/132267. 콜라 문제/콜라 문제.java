class Solution {
    public int coke(int a, int b, int n){
        return (n / a) * b;
    }
    public int solution(int a, int b, int n) {
        int answer = 0;        
        while(n >= a){
            answer += coke(a,b,n);
            n = (n / a) * b + (n % a);
        }
        return answer;
    }
}