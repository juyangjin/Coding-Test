import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int t1 = numbers[0] * numbers[1];
        int t2 = numbers[numbers.length-1] * numbers[numbers.length-2];
        if(t1 > t2) return t1;
        else return t2;
    }
}