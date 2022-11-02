class Solution {
    public int solution(int n, int k) {
        int tempk;
        tempk = n / 10;
        n = n*12000;
        k = k*2000;
        int result = n + k - (tempk*2000);
        return result;
    }
}