import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i=0;i<my_string.length();i++){
            if(Character.isDigit(my_string.charAt(i))){
                list.add(my_string.charAt(i) - '0');
            }
        }
        
        int[] answer = new int[list.size()];
        int len = 0;
        Collections.sort(list); //integer이면 Arrays.sort를 사용하고 ArrayList<Integer> 이면 Collections.sort를 사용한다.
        for(int a:list){
            answer[len++] = a;
        }
        
        return answer;
    }
}