import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String w = sc.nextLine();
        int[] ar = new int[26];
       
        for(int i=0;i<w.length();i++){
           int str = w.charAt(i);
            if(97 <= str && str <= 122){
                ar[str - 97]++;
            }else{
                ar[str - 65]++;
            }
        }
        int max = -1;
        char index = 0;
        
        for(int i=0;i<26;i++){
            if(ar[i]> max){
                max = ar[i];
                index = (char) (i+65);
            }else if(ar[i]==max){
                index = '?';
            }
        }
        System.out.println(index);
    }
}