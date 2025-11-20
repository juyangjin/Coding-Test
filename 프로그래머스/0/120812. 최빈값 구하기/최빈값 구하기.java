import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] array) {
        // 숫자 → 등장 횟수를 저장할 Map
        Map<Integer, Integer> countMap = new HashMap<>();

        /** 
         * 1. 배열을 한 번 돌면서 숫자당 등장 횟수를 셈
         *    getOrDefault는 없는 키면 0을 돌려줌
         */
        for (int num : array) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        int maxFreq = -1; // 최대로 등장한 횟수
        int mode = -1;    // 최빈값 후보
        boolean duplicateMax = false; // 최빈값이 여러 개인지 체크

        /**
         * 2. Map을 돌면서 최빈값(가장 많이 나온 숫자)을 찾음
         *    - 만약 같은 maxFreq를 가진 값이 또 나오면 중복 표시
         */
        for (int key : countMap.keySet()) {
            int freq = countMap.get(key);

            if (freq > maxFreq) {
                maxFreq = freq;
                mode = key;
                duplicateMax = false; // 새로 갱신되면 중복 아님
            } else if (freq == maxFreq) {
                duplicateMax = true; // 같은 등장 횟수 또 나오면 중복 최빈값
            }
        }

        // 3. 최빈값이 여러 개면 -1 리턴
        if (duplicateMax) return -1;

        return mode;
    }
}
