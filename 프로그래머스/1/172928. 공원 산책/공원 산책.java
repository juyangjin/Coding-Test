import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {

        int[] start = new int[2];  // 시작 위치

        // 방향 맵
        Map<String, int[]> dir = new HashMap<>();
        dir.put("N", new int[]{-1, 0});
        dir.put("S", new int[]{1, 0});
        dir.put("W", new int[]{0, -1});
        dir.put("E", new int[]{0, 1});

        // 1. 시작 위치 S 찾기
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length(); j++) {
                if (park[i].charAt(j) == 'S') {
                    start[0] = i;  // row
                    start[1] = j;  // col
                }
            }
        }

        // 2. routes 실행
        for (String r : routes) {

            String[] arr = r.split(" ");
            String op = arr[0];        // 방향
            int dist = Integer.parseInt(arr[1]); // 이동 거리

            int[] d = dir.get(op);     // 방향 벡터

            int nr = start[0];
            int nc = start[1];

            boolean ok = true;

            // 이동 가능 여부 검사
            for (int k = 0; k < dist; k++) {
                nr += d[0];
                nc += d[1];

                // 1) 공원 벗어나는지
                if (nr < 0 || nr >= park.length || nc < 0 || nc >= park[0].length()) {
                    ok = false;
                    break;
                }

                // 2) 장애물 있는지
                if (park[nr].charAt(nc) == 'X') {
                    ok = false;
                    break;
                }
            }

            // 이동 가능하면 start 업데이트
            if (ok) {
                start[0] = nr;
                start[1] = nc;
            }
        }

        return start;  // 최종 위치
    }
}
