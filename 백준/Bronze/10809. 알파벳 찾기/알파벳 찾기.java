import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] r = new int[26];
        
        for(int i=0;i<r.length;i++){
            r[i] = -1;
        }
        
        String w = sc.nextLine();
        
        for(int i=0;i<w.length();i++){
            char c = w.charAt(i);
            
            if(r[c - 'a'] == -1){
                r[c - 'a'] = i;
            }
        }
        
        for(int val: r){
            System.out.print(val + " ");
        }
    }
}