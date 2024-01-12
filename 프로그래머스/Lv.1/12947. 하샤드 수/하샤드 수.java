class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String n = Integer.toString(x);
        int[] num = new int[n.length()];
        int sum = 0;
        
        for(int i=0;i<n.length();i++){ //배열에 값 추가하기 
            num[i] = n.charAt(i)-48; //아스키코드값 빼기
        }
        
        for(int tmp : num){//자바 배열값 더하기
            sum += tmp;
        } 
        answer = x%sum == 0 ? true : false; //하샤드 수 구하기
        
        return answer;
    }
}