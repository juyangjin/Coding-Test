import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        
        int sum = n1 > 0 ? n2 > 0 ? 1 : 4 : n2 > 0 ? 2 : 3 ;
  
        System.out.println(sum);
    }
}