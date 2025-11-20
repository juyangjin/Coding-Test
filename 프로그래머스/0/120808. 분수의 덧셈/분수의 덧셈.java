class Solution {
    public static int GCD(int a,int b){
        if(a % b == 0){
            return b;
        }
            return GCD(b, a%b);    
    }
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int numer3 = (numer1 * denom2) + (numer2 * denom1);
        int denom3 =  denom1 * denom2;
        
        
        int gcd = GCD(numer3, denom3); 
        
        answer[0] = numer3 / gcd;
        answer[1] = denom3 / gcd;
        
        return answer;
    }
}