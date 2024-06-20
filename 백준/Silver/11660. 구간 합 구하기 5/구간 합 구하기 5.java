import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException{
    
        BufferedReader bf =
            new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str =
            new StringTokenizer(bf.readLine()); //빠른 연산 위한연산자들
            
        int N = Integer.parseInt(str.nextToken()); //2차원 배열 크기 받기
        int M = Integer.parseInt(str.nextToken()); //구간 합 질의 개수 받기
        int A[][] = new int[N+1][N+1];
        for(int i=1;i<=N;i++){ //배열의 크기만큼 
            str = new StringTokenizer(bf.readLine()); //str에 한 줄 받아오기
           for(int j=1;j<=N;j++){
                A[i][j] = Integer.parseInt(str.nextToken()); //A배열에 값 넣기
            }
        } //원본 배열 완성
        
        int D[][] = new int[N+1][N+1];   
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];
            } // 전체 구간 합 구하기
        }
        
        for(int i=1;i<=M;i++){
            str = new StringTokenizer(bf.readLine());
            int x1 = Integer.parseInt(str.nextToken());
            int y1 = Integer.parseInt(str.nextToken());
            int x2 = Integer.parseInt(str.nextToken());
            int y2 = Integer.parseInt(str.nextToken());
            int result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]; 
            System.out.println(result);
        }
    }
}