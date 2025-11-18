import java.util.HashMap;
import java.util.Map;

class Solution{
    public String solution(String[] survey, int[] choices) {

        Map<Character, Integer> score = new HashMap<>();
        score.put('R', 0);
        score.put('T', 0);
        score.put('C', 0);
        score.put('F', 0);
        score.put('J', 0);
        score.put('M', 0);
        score.put('A', 0);
        score.put('N', 0);

        for (int i = 0; i < survey.length; i++) {
            char left = survey[i].charAt(0);   // 비동의
            char right = survey[i].charAt(1);  // 동의
            int choice = choices[i];

            if (choice < 4) { // 비동의 (왼쪽 유형 점수 증가)
                score.put(left, score.get(left) + (4 - choice));
            } else if (choice > 4) { // 동의 (오른쪽 유형 점수 증가)
                score.put(right, score.get(right) + (choice - 4));
            }
        }

        StringBuilder sb = new StringBuilder();

        sb.append(getType(score, 'R', 'T'));
        sb.append(getType(score, 'C', 'F'));
        sb.append(getType(score, 'J', 'M'));
        sb.append(getType(score, 'A', 'N'));

        return sb.toString();
    }

    private char getType(Map<Character, Integer> score, char a, char b) {
        int scoreA = score.get(a);
        int scoreB = score.get(b);

        if (scoreA > scoreB) return a;
        else if (scoreB > scoreA) return b;
        else return a;  // 점수 같으면 사전순 앞 (문제에서 이미 a가 앞)
    }
}
