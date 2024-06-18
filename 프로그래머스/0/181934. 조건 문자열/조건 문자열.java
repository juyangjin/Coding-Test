class Solution {
    public int solution(String ineq, String eq, int n, int m) {
    
        if (ineq.equals(">")) { // ineq가 "">"인가?
            if (eq.equals("=")) { // eq가 "="인가?
                                return n >= m ? 1 : 0; //삼항연산자로 비교
                        } else if (eq.equals("!")) { //eq가 "!"인가?
                                return n > m ? 1 : 0;
                        }
                } else if (ineq.equals("<")) { // ineq가 "<" 인가?
                        if (eq.equals("=")) { // eq가 "=" 인가?
                                return n <= m ? 1 : 0;
                        } else if (eq.equals("!")) { //eq가 "!" 인가?
                                return n < m ? 1 : 0;
                        }
                }

                return 0; // 다 아니라면 0을 return하시오
    }
}