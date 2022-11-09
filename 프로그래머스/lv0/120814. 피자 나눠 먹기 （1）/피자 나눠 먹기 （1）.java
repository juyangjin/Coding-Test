class Solution {
    public int solution(int n) {
        int answer = n/7;
        int temp = n%7;
        if(temp == 0){
            return answer;
        } else {
            return answer + 1;
        }
    }
}