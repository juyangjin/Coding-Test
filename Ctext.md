# 코딩테스트 연습을 위한 페이지

## BaekjoonHub
* 백준 코딩사이트 링크 -> [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)  
* 백준 코딩테스트 결과 자동업로드  
  
## Programmers
* 프로그래머스 사이트 링크 -> [Programmers](https://programmers.co.kr)  
* 프로그래머스 코딩테스트 결과 자동업로드 

- __주의사항__ -> 백준 및 프로그래머스 업로드 시, 자동업로드가 제대로 되고 있는지 확인할 필요가 있음.
  
## 할일 목록
  ### - 22/10/05 -
   1.내 현재 실력에서 많이 부족함을 느끼기에 단계별로 진행할 예정  
   2.매일 JAVA 1문제씩 풀어보기(두 사이트 중 아무거나 1회씩 진행하기)  
   3.주 1회 Python 문제 풀기(월요일 예정)  
   4.주 1회 C++ 문제 풀기(금요일 예정) > C언어와 유사하지만 Class가 추가된 부분이 있다고 하니, 인터넷 강의 참고하여 공부하기  
   5.기존 자바 책 공부도 꼭 하기  
    
  ### - 22/10/25
   1.프로그래머스 0단계는 11월 중순 이전에 마치도록 하기(하루 5개는 해야하지만, 그래도 어쩔 수 없다!)  
   2.백준은 아직 조금 어렵지만, 그래도 꾸준히 도전하기  
   3.코딩테스트 순서도는 `JAVA > C > Python > C++ > Swift` __일단 JAVA 0단계를 마치면 C언어 0단계와 JAVA 1단계 병행하는 식으로 중첩공부__

   ### 백준 2042번 eclipse에서는 이상없이 실행되지만 백준에서는 에러나는 코드
```JAVA
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader bf =
            new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st =
            new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] A = new int[N+1];
        int[] S = new int[N+1];
           
        for(int i=1;i<=N;i++){
            st = new StringTokenizer(bf.readLine());
            A[i] = Integer.parseInt(st.nextToken());
        }//원본 배열 만들기

        for(int i=1;i<=K+M;i++){
            	st = new StringTokenizer(bf.readLine());
                int one = Integer.parseInt(st.nextToken());
                int two = Integer.parseInt(st.nextToken());
                int three = Integer.parseInt(st.nextToken());
                
                if(one == 1){
                    A[two] = three;
                    for(int q=1;q<=N;q++){
                        S[q] = S[q-1] + A[q];
                    }//합배열 만들기 
                }
                else if(one == 2){
                   System.out.println(S[three] - S[two-1]);
                }		
        }
    }
}
```


#
# 백준, 프로그래머스 문제 풀이 목록

## 📚 백준 문제 풀이 목록

## 📚 프로그래머스 문제 풀이 목록
