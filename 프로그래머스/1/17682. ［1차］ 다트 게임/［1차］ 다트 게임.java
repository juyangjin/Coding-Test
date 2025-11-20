import java.util.*;

class Solution {
    public int solution(String dartResult) {
        List<Integer> scores = new ArrayList<>();
        int num = 0; // 현재 숫자를 저장

        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);

            // 숫자 처리 (10도 가능)
            if (Character.isDigit(c)) {
                // 이전 숫자가 있을 때 10인지 판단
                if (c == '0' && num == 1) {
                    num = 10; // 10 처리
                } else {
                    num = c - '0';
                }
            } 
            // 보너스 처리 (제곱 적용)
            else if (c == 'S' || c == 'D' || c == 'T') {
                if (c == 'S') num = (int) Math.pow(num, 1);
                else if (c == 'D') num = (int) Math.pow(num, 2);
                else if (c == 'T') num = (int) Math.pow(num, 3);

                scores.add(num); // 점수 저장
            } 
            // 옵션 처리
            else if (c == '*' || c == '#') {
                int lastIndex = scores.size() - 1;

                if (c == '*') {
                    // 현재 점수 2배
                    scores.set(lastIndex, scores.get(lastIndex) * 2);

                    // 이전 점수가 있다면 그것도 2배
                    if (lastIndex > 0) {
                        scores.set(lastIndex - 1, scores.get(lastIndex - 1) * 2);
                    }
                } else if (c == '#') {
                    // 현재 점수 -1배
                    scores.set(lastIndex, scores.get(lastIndex) * -1);
                }
            }
        }

        // 모든 점수를 더함
        return scores.stream().mapToInt(Integer::intValue).sum();
    }
}
