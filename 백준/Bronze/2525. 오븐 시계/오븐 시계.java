import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int m = sc.nextInt();
        int c = sc.nextInt();
        
        t += c / 60;
        m += c % 60;
        
        if(m>=60){
            t += 1;
            m -= 60;
        }
        if(t >= 24){
            t -= 24;
        }
        System.out.println(t + " " + m);
    }
}