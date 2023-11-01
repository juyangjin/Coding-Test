class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int val1 = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int val2 = Integer.parseInt(Integer.toString(b) + Integer.toString(a));
        if(val1 >= val2){
            answer = val1;
        }
        else{
            answer = val2;
        }
        return answer;
    }
}