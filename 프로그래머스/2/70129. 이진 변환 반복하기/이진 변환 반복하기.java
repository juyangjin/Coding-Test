class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int before = s.length(); //s의 원래 길이
            s = s.replace("0", ""); //0 제거
            answer[1] += before - s.length(); //제거된 0의 개수를 누적해서 넣음
            s = Integer.toBinaryString(s.length()); //이진수로 바꾼 s
            answer[0]++; //answer의 첫번째 인덱스의 값을 하나 늘림
        }
        
        return answer;
    }
}
