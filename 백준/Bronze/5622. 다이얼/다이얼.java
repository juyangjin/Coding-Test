import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String w = sc.nextLine();
        int cnt = 0;
        
        for(int i=0;i<w.length();i++){
            if((int) w.charAt(i) <= 79 && (int) w.charAt(i) >= 65 ){
                cnt = cnt + (((int) w.charAt(i) - 65) / 3) + 3;
            }if((int) w.charAt(i) >= 87 && (int) w.charAt(i) <= 90){
                cnt += 10;
            }if((int) w.charAt(i) >= 84 && (int) w.charAt(i) <= 86){
                cnt += 9;
            }if((int) w.charAt(i) >= 80 && (int) w.charAt(i) <= 83){ 
                cnt += 8;
                 }
        } System.out.print(cnt);
    }
}