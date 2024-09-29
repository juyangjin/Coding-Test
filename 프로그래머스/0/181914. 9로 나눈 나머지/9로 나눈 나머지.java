class Solution {
    public int solution(String number) {
        int answer = 0;
        
        for(int i=0;i<number.length();i++){
            answer += Character.getNumericValue(number.charAt(i));
        }
        
        answer %= 9;
        return answer;
    }
}