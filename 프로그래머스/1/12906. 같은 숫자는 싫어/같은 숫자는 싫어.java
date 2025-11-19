import java.util.*;

class Solution {

    /**
     * 연속된 중복 숫자를 제거하는 메서드
     * @param arr 입력 배열
     * @return 연속 중복 제거 후 배열
     */
    public int[] solution(int[] arr) {

        /** 
         * 결과를 임시로 담아둘 리스트
         * - 이유: 결과 크기를 미리 알 수 없기 때문에
         * - 마지막에 정확한 크기의 int[] 로 변환할 예정
         */
        List<Integer> list = new ArrayList<>();

        /**
         * 바로 직전에 본 숫자를 저장하는 변수
         * - 문제 특성상 숫자는 0~9라서 -1은 절대 나오지 않는 값 → 안전한 초기값
         * - 첫 번째 숫자는 무조건 추가되도록 하는 역할
         */
        int prev = -1;

    
        for (int num : arr) {

            /**
             * 현재 숫자(num)가 이전 숫자(prev)와 다를 때만 리스트에 추가
             * - 즉, 연속해서 같은 값이 들어오면 무시
             */
            if (num != prev) {
                list.add(num);   // 새로운 값 발견 → 결과 리스트에 추가
                prev = num;      // 현재 숫자를 '이전 숫자'로 업데이트
            }
            // 같으면 아무 것도 하지 않고 넘어감
        }

        /**
         * List<Integer> → int[] 변환
         * - list 크기만큼 정확한 크기의 배열 생성
         */
        int[] answer = new int[list.size()];

        /**
         * list 안의 값을 하나씩 배열로 복사
         * - Integer → int로 자동 언박싱됨
         */
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
