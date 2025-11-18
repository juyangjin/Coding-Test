import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        // 1. 크기별 개수를 세기 위한 맵 (크기 -> 개수)
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int size : tangerine) {
            // size 크기의 귤 개수를 1 증가
            countMap.put(size, countMap.getOrDefault(size, 0) + 1);
        }
        
        // 2. 크기별 "개수"만 모아서 리스트로 만들기
        List<Integer> counts = new ArrayList<>(countMap.values());
        
        // 3. 많이 있는 크기부터 쓰고 싶으니까 개수 기준 내림차순 정렬
        counts.sort(Collections.reverseOrder());
        
        int picked = 0;  // 지금까지 고른 귤 개수 합
        int kinds = 0;   // 사용한 귤 크기 종류 수
        
        // 4. 큰 개수부터 차례대로 더해가며 k 이상이 될 때까지 반복
        for (int c : counts) {
            picked += c; // 이 크기 전부 다 가져온다고 가정
            kinds++;     // 크기 종류 하나 사용
            
            if (picked >= k) {
                // k개 이상 채웠으면 종료
                break;
            }
        }
        
        // 5. 사용한 "크기 종류 수"가 답
        return kinds;
    }
}
