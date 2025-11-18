class Solution {
    public String solution(String s) {
        String answer = "";
        
        s = s.toLowerCase();
        
        char[] arr = s.toCharArray();

        for (int i = 0; i < arr.length; i++) {
            if (i == 0 || arr[i - 1] == ' ') {
                arr[i] = Character.toUpperCase(arr[i]);
            }
        }
        
        answer = String.valueOf(arr);
        return answer;
    }
}