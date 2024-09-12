import java.util.Arrays;

class Solution {
    
    public static int[] removeElement(int[] numlist,int item){
        return Arrays.stream(numlist)
            .filter(i -> i != item)
            .toArray();
    }
    
    public int[] solution(int n, int[] numlist) {
        int[] answer = new int[numlist.length];
        
        for(int i=0;i<numlist.length;i++){
            answer[i] += numlist[i] % n == 0 ? numlist[i] : 0;
        }

        int item = 0;
        answer = removeElement(answer,item);
        
        return answer;
    }
}