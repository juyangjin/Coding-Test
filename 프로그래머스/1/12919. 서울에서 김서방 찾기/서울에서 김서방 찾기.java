class Solution {
    public String solution(String[] seoul) {
        int num = 0;;
        String answer = "";
        
        for(int i=0;i<seoul.length;i++){
            num = seoul[i].equals("Kim") ? i : num;
            answer = String.format("김서방은 %d에 있다",num);
            
        }
        return answer;
    }
}