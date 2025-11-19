import java.util.*;

class Solution {

    // 괄호 문자열이 올바른지 검사하는 메서드
    private boolean isValid(String str, Map<Character, Character> pair) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);

            // 1) 여는 괄호면 무조건 스택에 넣기
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } 
            // 2) 닫는 괄호면 짝이 맞는지 검사
            else {
                // 스택이 비어 있으면 짝이 될 여는 괄호가 없음 → 실패
                if (stack.isEmpty()) return false;

                char top = stack.pop();      // 스택에서 마지막 여는 괄호 하나 꺼내고
                // pair.get(c) : 현재 닫는 괄호 c가 기대하는 "여는 괄호"
                if (pair.get(c) != top) return false;  // 짝이 안 맞으면 실패
            }
        }

        // 전부 다 돌았을 때 스택이 비어 있어야 완벽하게 짝이 맞는 것
        return stack.isEmpty();
    }

    public int solution(String s) {
        int answer = 0;  // 올바른 회전 개수 세는 변수

        // 닫는 괄호 -> 여는 괄호 매핑
        Map<Character, Character> pair = new HashMap<>();
        pair.put(')', '(');
        pair.put(']', '[');
        pair.put('}', '{');

        int n = s.length();

        // i번 왼쪽으로 회전한 문자열들을 전부 검사
        for (int i = 0; i < n; i++) {
            // s를 i만큼 왼쪽으로 회전한 문자열
            String rotated = s.substring(i) + s.substring(0, i);

            // 회전된 문자열이 올바른 괄호 문자열이면 +1
            if (isValid(rotated, pair)) {
                answer++;
            }
        }

        return answer;
    }
}
