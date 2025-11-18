import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {

        // 1. 신고 기록 (중복 제거)
        Map<String, Set<String>> reportMap = new HashMap<>();
        for (String id : id_list) {
            reportMap.put(id, new HashSet<>());
        }

        for (String r : report) {
            String[] arr = r.split(" ");
            String from = arr[0];
            String to = arr[1];

            reportMap.get(from).add(to); // 중복 자동 제거
        }

        // 2. 신고당한 횟수 세기
        Map<String, Integer> count = new HashMap<>();
        for (String id : id_list) {
            count.put(id, 0);
        }

        // 각 사람이 신고한 리스트 순회
        for (String from : id_list) {
            for (String to : reportMap.get(from)) {
                count.put(to, count.get(to) + 1);
            }
        }

        // 3. 정지된 사람 리스트 만들기
        Set<String> banned = new HashSet<>();
        for (String id : id_list) {
            if (count.get(id) >= k) {
                banned.add(id);
            }
        }

        // 4. 최종 메일 카운트
        int[] answer = new int[id_list.length];

        for (int i = 0; i < id_list.length; i++) {
            String user = id_list[i];

            int mail = 0;
            for (String target : reportMap.get(user)) {
                if (banned.contains(target)) {
                    mail++;
                }
            }
            answer[i] = mail;
        }

        return answer;
    }
}
