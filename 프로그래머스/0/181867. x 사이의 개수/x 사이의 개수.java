class Solution {
    public int[] solution(String myString) {
        String[] len = myString.split("x",-1);
        int[] answer = new int[len.length];
        
        for(int i=0;i<answer.length;i++){
            answer[i] = len[i].length();
        }
        
        return answer;
    }
}