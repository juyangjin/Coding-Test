class Solution {
    public int solution(int hp) {
        int q = hp / 5;
        int s = hp % 5;
        int answer =  hp % 5 != 0 ?
            s % 3 != 0 ?
            q + (s/3) + s % 3 : q + (s/3) : q;
        
        return answer;
    }
}