class Solution {
    public int[] solution(int brown, int yellow) {

        int total = brown + yellow;  // 전체 격자 수

        // width >= height 조건이 있으므로 width를 큰 값부터 찾는 것이 일반적
        for (int height = 3; height <= total; height++) {
            if (total % height == 0) { // 나누어떨어지면 width 후보
                int width = total / height;

                // 노란 영역 크기 계산: (width - 2) * (height - 2)
                // 이 값이 yellow와 같으면 정답
                if ((width - 2) * (height - 2) == yellow) {
                    return new int[] { width, height };
                }
            }
        }

        return null; // 도달 불가능(문제 조건상 항상 해답 존재)
    }
}
