import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        List<Integer> R = Arrays.asList(3, 6, 9);
        List<Integer> L = Arrays.asList(1, 4, 7);
        List<Integer> C = Arrays.asList(2, 5, 8, 0);

        // 손 위치 좌표 (row, col)
        int[] leftPos = {3, 0};   // * = (3,0)
        int[] rightPos = {3, 2};  // # = (3,2)

        StringBuilder sb = new StringBuilder();

        for (int num : numbers) {

            // 1) 오른쪽 라인: 3,6,9
            if (R.contains(num)) {
                sb.append("R");
                rightPos = toPos(num);
                continue;
            }

            // 2) 왼쪽 라인: 1,4,7
            if (L.contains(num)) {
                sb.append("L");
                leftPos = toPos(num);
                continue;
            }

            // 3) 가운데 라인: 2,5,8,0 → 거리 비교
            if (C.contains(num)) {
                int[] target = toPos(num);

                int leftDist = dist(leftPos, target);
                int rightDist = dist(rightPos, target);

                if (leftDist < rightDist) {
                    sb.append("L");
                    leftPos = target;

                } else if (rightDist < leftDist) {
                    sb.append("R");
                    rightPos = target;

                } else { // 같으면 hand 기준
                    if (hand.equals("left")) {
                        sb.append("L");
                        leftPos = target;
                    } else {
                        sb.append("R");
                        rightPos = target;
                    }
                }
            }
        }

        return sb.toString();
    }

    // 숫자를 키패드 좌표로 변환
    private int[] toPos(int num) {
        if (num == 0) return new int[]{3, 1};
        int row = (num - 1) / 3;
        int col = (num - 1) % 3;
        return new int[]{row, col};
    }

    // 맨해튼 거리 계산
    private int dist(int[] hand, int[] target) {
        return Math.abs(hand[0] - target[0]) + Math.abs(hand[1] - target[1]);
    }
}
