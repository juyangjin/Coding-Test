class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int sum = 0;
        
        for(int i=0;i<arr.length;i++){
           sum += arr[i];
        }
        return answer = (double)sum/(arr.length); //sum/(arr.length) 앞에 double로 실수표현
    }
}