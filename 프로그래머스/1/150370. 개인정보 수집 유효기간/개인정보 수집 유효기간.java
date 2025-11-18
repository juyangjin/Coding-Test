import java.util.*;

class Solution {
    
    // 날짜를 총 일수로 변환하는 함수
    private int toDays(String date) {
        String[] arr = date.split("\\.");
        int y = Integer.parseInt(arr[0]);
        int m = Integer.parseInt(arr[1]);
        int d = Integer.parseInt(arr[2]);
        return y * 12 * 28 + m * 28 + d;
    }

    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> result = new ArrayList<>();
        int todayDays = toDays(today);

        // terms 파싱
        Map<String, Integer> termMap = new HashMap<>();
        for (String t : terms) {
            String[] parts = t.split(" ");
            termMap.put(parts[0], Integer.parseInt(parts[1]));
        }

        // privacies 검사
        for (int i = 0; i < privacies.length; i++) {
            String[] p = privacies[i].split(" ");
            String date = p[0];
            String type = p[1];

            int collected = toDays(date);
            int months = termMap.get(type);

            int expire = collected + months * 28 - 1; // 진짜 만료일

            if (expire < todayDays) {
                result.add(i + 1); // 번호는 1번부터
            }
        }

        // 리스트 → 배열 변환
        return result.stream().mapToInt(x -> x).toArray();
    }
}
