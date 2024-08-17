import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n[] = new int[10];
        
        for(int i=1;i<=9;i++){
            n[i] = sc.nextInt();
        }
        int max = n[1];
        int c = 1;
        for(int j=1;j<=9;j++){
            if(max < n[j]){
                max = n[j];
                c = j;
            }
        }
        System.out.print(max + "\n" + c);
    }
}