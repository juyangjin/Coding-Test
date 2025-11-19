import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        
        // 각 스테이지(1~N)의 실패한 사람 수를 저장
        int[] fail = new int[N + 1];
        
        // 각 스테이지 번호가 나올 때마다 count
        for (int s : stages) {
            if (s <= N) {  
                fail[s]++;  // 해당 스테이지에서 실패(도전 중)
            }
        }
        
        // 실패율 저장을 위한 리스트
        List<double[]> list = new ArrayList<>();
        
        // 도달한 사람 수 = 처음엔 전체 유저 수
        int players = stages.length;
        
        for (int stage = 1; stage <= N; stage++) {
            
            if (players == 0) { 
                // 더 이상 도달한 사람이 없으면 실패율 0
                list.add(new double[]{stage, 0});
                continue;
            }
            
            double failureRate = (double) fail[stage] / players;
            
            list.add(new double[]{stage, failureRate});
            
            // 다음 스테이지는 현재 스테이지에서 실패한 사람을 제외한 만큼만 도달함
            players -= fail[stage];
        }
        
        // 실패율 기준으로 내림차순 정렬
        // 실패율 같으면 스테이지 번호 오름차순
        Collections.sort(list, (a, b) -> {
            if (b[1] == a[1]) return (int)(a[0] - b[0]);
            return Double.compare(b[1], a[1]);
        });
        
        // 정답 배열 만들기
        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = (int) list.get(i)[0];
        }
        
        return answer;
    }
}
