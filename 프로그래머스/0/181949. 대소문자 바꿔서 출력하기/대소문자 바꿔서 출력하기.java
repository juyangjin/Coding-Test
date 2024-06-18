import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        String result = "";
        int temp = 0;
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for(int i=0; i<a.length();i++){
            temp = (int)a.charAt(i); //문자열을 int형으로 변환
            if((temp >= 65) && (temp <= 90)){
                result += (char)(temp +32);
            }
            
            else if((97<=temp) && (temp <= 122)){
                result += (char)(temp -32);
            }
            
            else{
                result +=(char)temp;
            }
        }
        System.out.print(result);
    }
}