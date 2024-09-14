import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int sum = n % 2;
        
        if(sum == 1){
            System.out.print(n + " is odd");
        }
        else{
            System.out.print(n + " is even");
        }
    }
}