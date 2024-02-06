class Solution {
    public String[] solution(String[] names) {
        String[] answer = names.length%5 == 0 ? new String[names.length/5] : new String[(names.length/5)+1];
        for(int i=0,j=0;i<names.length;j++){
            answer[j] = names[i];
            i += 5;
        }
        
        return answer;
    }
}