class Solution {
    boolean solution(String s) {
        char a = '(';
        char b = ')';
        int count = 0;
        
        if(s.charAt(0) == b) return false;
        if(s.charAt(s.length()-1) == a) return false;
        
        for(int i=0;i<s.length();i++) {
            if(s.charAt(i) == a){
                count++; 
            } 
            if(s.charAt(i) == b){
                count--;
                if(count < 0){
                return false;
                }
            }
        }
        return count == 0;
    }
}