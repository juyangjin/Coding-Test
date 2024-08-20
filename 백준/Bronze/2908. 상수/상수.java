import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        int c = 0;
        int d = 0;

        for(int i=0;i<3;i++){
            c = (c * 10) + (a % 10);
            a = a/10;
        }
        
        for(int i=0;i<3;i++){
            d = (d * 10) + (b % 10);
            b = b/10;
        }  
        System.out.print(Math.max(c,d));
    }
}