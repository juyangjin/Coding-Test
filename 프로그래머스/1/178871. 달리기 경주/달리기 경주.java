import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {

        // 이름 -> 현재 등수
        Map<String, Integer> rank = new HashMap<>();

        // 초기 세팅: players 배열 인덱스 = 현재 등수
        for (int i = 0; i < players.length; i++) {
            rank.put(players[i], i);
        }

        // 콜마다 앞지르기 처리
        for (String player : callings) {
            int current = rank.get(player);  // 현재 등수
            int prev = current - 1;          // 바로 앞 등수

            String frontPlayer = players[prev]; // 앞사람 이름

            // players 배열에서 둘의 자리 교환
            players[prev] = player;
            players[current] = frontPlayer;

            // rank 맵에서도 둘의 등수 업데이트
            rank.put(player, prev);
            rank.put(frontPlayer, current);
        }

        return players;
    }
}
