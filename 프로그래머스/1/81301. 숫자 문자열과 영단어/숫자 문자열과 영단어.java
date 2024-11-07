class Solution {
    public int solution(String s) {
        String[] name = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        for(int i=0;i<name.length;i++){
            if(s.contains(name[i])) {
        		s = s.replace(name[i], Integer.toString(i));
        	}
        }
        return Integer.parseInt(s);
    }
}