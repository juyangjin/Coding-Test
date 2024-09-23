class Solution {
    public String solution(String myString) {
        String a = "a";
        myString = myString.toLowerCase();
        String answer = myString.replace(a, a.toUpperCase());
        return answer;
    }
}