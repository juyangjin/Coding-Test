class Solution {
    public int solution(String[][] board, int h, int w) {
        /**
         * 상하좌우 이동을 위한 배열
         * dh: 행(row) 이동 값
         * dw: 열(column) 이동 값
         *
         * (0, 1)  → 오른쪽
         * (1, 0)  → 아래
         * (-1, 0) → 위
         * (0, -1) → 왼쪽
         */
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};

        int h_check = 0; // 이동 후 검사할 행
        int w_check = 0; // 이동 후 검사할 열
        
        // 기준 칸의 색
        String color = board[h][w];

        int n = board.length; // 보드 한 변의 길이
        int answer = 0;       // 같은 색인 이웃 칸 수
        
        // 네 방향(상하좌우) 검사
        for (int i = 0; i < 4; i++) {

            // 새로운 좌표 계산
            h_check = h + dh[i];
            w_check = w + dw[i];

            /**
             * 보드 범위 내인지 검사
             * 0 ≤ h_check < n
             * 0 ≤ w_check < n
             * → 인덱스가 보드를 벗어나면 접근 불가이므로 제외
             */
            if (h_check >= 0 && h_check < n && w_check >= 0 && w_check < n) {

                /**
                 * 기준 칸(board[h][w])과
                 * 이웃 칸(board[h_check][w_check])의 색이 같으면 카운트 증가
                 */
                if (color.equals(board[h_check][w_check])) {
                    answer++;
                }
            }
        } 
        
        // 최종적으로 같은 색인 이웃 칸 개수 반환
        return answer;
    }
}
