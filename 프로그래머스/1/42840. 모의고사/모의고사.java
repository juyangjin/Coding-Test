import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] su1 = {1,2,3,4,5};
        int[] su2 = {2,1,2,3,2,4,2,5};
        int[] su3 = {3,3,1,1,2,2,4,4,5,5}; //수포자 3명의 찍기유형
        int[] result = new int[3]; // 3명의 점수가 들어갈 배열 
        
        for(int i=0;i<answers.length;i++){
            if(answers[i] == su1[i%5]) result[0]++;
            if(answers[i] == su2[i%8]) result[1]++; 
            if(answers[i] == su3[i%10]) result[2]++; 
        }  //수포자 3명의 배열이 반복되어야 하므로 i%배열갯수로 나머지값만 연산할 수 있게한다. 수가 맞다면 그에 따라 result의 각 인덱스값이 1씩 늘어난다.
        
        int M = Math.max(result[0],Math.max(result[1],result[2])); 
        //Math를 사용해 최댓값 계산
        List<Integer> answer = new ArrayList<>();
        //ArrayList형식으로 answer 선언
        for(int i=0;i<result.length;i++){
            if(M == result[i]) answer.add(i+1);
        } // 최댓값 M과 result[i] 값이 동일하다면 answer에 해당 인덱스의 값+1을 추가한다.(0부터 인덱스가 시작되기 때문)
        
        int[] sum = answer.stream() //answer을 stream으로 변환
                    .mapToInt(i -> i) //mapToInt로 인덱스 값을 할당
                    .toArray(); //ArrayList형식에서 변환되는 것이기 때문에 toArray();로 마무리
        
        return sum; //int 배열인 sum을 return
    }
}