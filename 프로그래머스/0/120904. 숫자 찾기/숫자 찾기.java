class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String ar = Integer.toString(num);
        String[] arr = ar.split("");
        
        for(int i=0;i<arr.length;i++){
            if(arr[i].equals(Integer.toString(k))) return i+1;
        }
        
        return answer;
    }
}