import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] student = new int[n];
        Arrays.fill(student, 1);
        
        for(int l : lost){
            student[l-1]--; //체육복이 도난되면 값 -1
        }
        for(int r : reserve){
            student[r-1]++; //체육복이 여벌이면 값 +1
        }
        
        for(int i=0;i<student.length;i++){
            if(student[i] == 0) {
                if(i > 0 && student[i-1] == 2){
                    student[i]++;
                    student[i-1]--;
                }else if(i < student.length - 1&& student[i+1] == 2){
                    student[i]++;
                    student[i+1]--;
                }
            }
        }
        for(int s: student){
            if(s > 0){
                answer++;
            }
        }
        
        return answer;
    }
}