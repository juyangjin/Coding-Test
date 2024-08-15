import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if(n % 400 == 0){
            System.out.print(1);
        } else if(n % 4 == 0 && n % 100 != 0) { 
            System.out.print(1);
        } else { 
            System.out.print(0);
        }
    } 
}