class Solution {
    public String solution(String my_string, String letter) {
        String Remove = letter;
 
        for (char c : Remove.toCharArray()) {
            my_string = my_string.replace(String.valueOf(c), "");
        }
        return my_string;
    }
}