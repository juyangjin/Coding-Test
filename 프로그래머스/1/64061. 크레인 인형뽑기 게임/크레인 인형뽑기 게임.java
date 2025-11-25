import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        
        for(int m: moves){
            for(int i=0;i<board.length;i++) {
                if(board[i][m-1] != 0) {
                    System.out.println(board[i][m-1]);
                    if(!stack.isEmpty()){
                        if(stack.peek() == board[i][m-1]){
                            stack.pop();
                            answer += 2;
                            board[i][m-1] = 0;
                            break;
                        }else {
                            stack.push(board[i][m-1]);
                            board[i][m-1] = 0;
                            break;
                        }
                    }else {
                        stack.push(board[i][m-1]);
                        board[i][m-1] = 0;
                        break;
                    }
                    
                }
            }
        }
            
        return answer;
    }
}