import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        
        int one = (n2 % 10) * n1;
        int ten = (n2 % 100 / 10) * n1;
        int hun = (n2 / 100) * n1;
        
        System.out.println(one);
        System.out.println(ten);
        System.out.println(hun);
        System.out.println(n1 * n2);
    }
}