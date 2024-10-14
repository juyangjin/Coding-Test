class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = included[0] == true ? a : 0;
        int tmp = d;
        
        for(int i=1;i<included.length;i++){
            if(i == 1) d = a + d;
            if(included[i] == true){
                answer += d;
            }
            d += tmp;
        }
        
        return answer;
    }
}