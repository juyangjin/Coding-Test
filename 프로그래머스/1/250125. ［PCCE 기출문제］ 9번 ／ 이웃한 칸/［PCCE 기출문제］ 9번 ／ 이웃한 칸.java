class Solution {
    public int solution(String[][] board, int h, int w) {
        //확인할 높이와 길이
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};
        int h_check = 0;
        int w_check = 0;
        
        //현재 컬러
        String color = board[h][w];
        int n = board.length;
        int answer = 0;
        
        for(int i= 0;i<4;i++) {
            h_check = h + dh[i];
            w_check = w + dw[i];
            if(h_check >= 0 && h_check < n && w_check >= 0 && w_check < n) {
                if(board[h][w].equals(board[h_check][w_check])) {
                answer++;
                }
            }
        } 
        
        return answer;
    }
}