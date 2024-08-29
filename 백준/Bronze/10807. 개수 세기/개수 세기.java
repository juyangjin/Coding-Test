import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] n = new int[sc.nextInt()];
            
        for(int i=0;i<n.length;i++){
            n[i] = sc.nextInt();
        }
        int v = sc.nextInt();
        int sum = 0;
        
        for(int i=0;i<n.length;i++){
            sum = n[i] == v? sum+1 : sum;
        }
        System.out.println(sum);
    }
}