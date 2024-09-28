class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] tmp = binomial.split(" ");
        
        int a = Integer.parseInt(tmp[0]);
        int b = Integer.parseInt(tmp[2]);
        
        if(tmp[1].equals("*")) answer = a * b ;
        else if(tmp[1].equals("-")) answer = a - b ;
        else if(tmp[1].equals("+")) answer = a + b ;
       return answer;  
    }
   
}