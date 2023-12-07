class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        myString = myString.replaceAll("A","b");
        myString = myString.replaceAll("B","A");
        myString = myString.replaceAll("b","B");
        
        answer = myString.contains(pat) ? 1 : 0;
        
        return answer;
    }
}