import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = 1;
        int sIdx = 1;
        int eIdx = 1; 
        int sum = 1;
        
        while (eIdx !=N){
            if(sum == N){
                C++;
                eIdx++;
                sum += eIdx;
            }
            else if(sum > N){
                sum -= sIdx;
                sIdx++;
            }
            else { 
                eIdx++;
                sum += eIdx;
            }
        }
        System.out.println(C);
    }
}