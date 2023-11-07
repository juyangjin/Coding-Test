class Solution {
    public int solution(int n) {
        int answer= 0;
        
        for(int i=n-1; i>0; i--){       
            answer = n % i == 1 ? i : answer;
        }
        return answer;
    }
}

// import java.util.stream.IntStream;

// class Solution {
//     public int solution(int n) {
//         return IntStream.range(2, n).filter(i -> n % i == 1).findFirst().orElse(0);
//     }
// } 스트림 공부용