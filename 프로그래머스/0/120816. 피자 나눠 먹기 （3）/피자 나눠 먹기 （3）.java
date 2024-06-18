class Solution {
    public int solution(int slice, int n) {
        int result = 0;
        int remainder = n % slice;
        int temp = n / slice;
        if(remainder==0){
            result = temp;
        } else {
            result = temp + 1;
        }
        return result;
    }
}