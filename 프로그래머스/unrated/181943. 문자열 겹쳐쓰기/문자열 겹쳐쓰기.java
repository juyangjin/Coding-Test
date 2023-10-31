class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        
        String result =  my_string.substring(0, s) + overwrite_string;
        
        if(my_string.length() > result.length()) {
            result += my_string.substring(result.length());
        }
        return result;
    }
}