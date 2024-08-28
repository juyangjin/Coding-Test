import java.util.Scanner;

public class Main{
    public static int prime(int x){
    	if(x==1) return 0;
        for(int i=2; i*i<=x;i++){
            if(x%i==0) return 0;
        }  
        return 1;
    } 
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        
        for(int i=0;i<n;i++){
            int x = sc.nextInt();
            cnt += prime(x);
        }
        System.out.println(cnt);
    }
}