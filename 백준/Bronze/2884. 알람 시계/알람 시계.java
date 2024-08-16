import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int sh,sm = 0;
        
        if(m>=45){
            System.out.println(h + " " + (m-45));
        }else{
            sh = h == 0 ? 23 : h-1; 
            sm = 60 - (45 - m);
            System.out.println(sh + " " + sm);
        }
    }
}