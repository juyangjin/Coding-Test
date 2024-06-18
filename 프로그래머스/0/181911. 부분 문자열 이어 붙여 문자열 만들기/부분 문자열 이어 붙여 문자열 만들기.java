class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        
        for(int i=0;i<my_strings.length;i++){
            String p = my_strings[i];
            
            answer += p.substring(parts[i][0],parts[i][1]+1);
        }
        return answer;
    }
}