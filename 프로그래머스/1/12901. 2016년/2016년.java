class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] days = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int tmp = 0;
        
        for(int i=0;i<a-1;i++){
            tmp += month[i];
        }
        
        tmp += b-1;
        tmp %= 7;
        
        answer = days[tmp];
        
        return answer;
    }
}