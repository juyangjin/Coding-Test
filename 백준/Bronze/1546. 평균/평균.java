import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long max = 0;
        long sum = 0;
        int A[] = new int[N];
        
        for(int i=0;i<N;i++){
            A[i] = sc.nextInt();
        }
        
        for(int j=0;j<N;j++){
            if(A[j] > max) max = A[j];
            sum += A[j];
        }
        System.out.println(sum * 100.0 / max / N);
    }
}