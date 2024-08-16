import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
         
        for(int i=0;i<n;i++){
            a[i] = sc.nextInt();
        }
        int max = a[0];
        int min = a[0];
        for(int j=0;j<n;j++){
            int t = a[j];
            max = max > t ? max : t;
            min = min < t ? min : t;
        }
        System.out.println(min + " " + max);
    }
}