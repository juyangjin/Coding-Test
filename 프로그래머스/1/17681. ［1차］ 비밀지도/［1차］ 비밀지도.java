class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String[] binary = new String[n];
        
        for(int i=0;i<arr1.length;i++) {
            int x = arr1[i] | arr2[i];
            String bin = Integer.toBinaryString(x);
            bin= String.format("%" + n + "s", bin).replace('0', ' ').replace('1', '#');
            answer[i] = bin;
        }
        
        return answer;
    }
}