class Solution {
    public static int GCD(int a,int b){//확장 유클리드 호제법을 이용
        if(a % b == 0){
            return b;
        }
            return GCD(b, a%b);    
    }
    public int[] solution(int n, int m) {
        int g = GCD(n, m);
        int[] answer = {g, (n*m)/g};
        
        return answer;
    }
}