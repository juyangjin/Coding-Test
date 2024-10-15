class Solution {
    public String solution(int age) {
        String[] ageArr = String.valueOf(age).split("");
        String ar = "abcdefghij";
        String answer = "";
        
        for (int i = 0; i < ageArr.length; i++) {
        	answer += ar.charAt(Integer.valueOf(ageArr[i]));
        } 
        return answer;
    }
}