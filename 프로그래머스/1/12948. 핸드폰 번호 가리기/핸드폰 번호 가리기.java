class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String[] num = phone_number.split("");
        int n = num.length;
        
        for(int i = 0; i < n; i++) {
            answer += i < n-4 ? "*" : num[i];
        }
        return answer;
    }
}