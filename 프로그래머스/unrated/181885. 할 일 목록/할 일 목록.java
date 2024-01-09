import java.util.Arrays;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        String[] answer = new String[todo_list.length];
    
        for(int i=0;i<todo_list.length;i++){
             answer[i] = finished[i] == true ? "0" : todo_list[i]; 
        }
        
        answer = Arrays.stream(answer)
            .filter(item -> !item.equals("0"))
            .toArray(String[]::new);
        
        return answer;
    }
}