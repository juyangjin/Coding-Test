import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = 
            new BufferedReader(new InputStreamReader(System.in));
        
        int[] arr = new int[10];
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        int sum = a * b * c;
        String str = Integer.toString(sum);
        
        for(int i=0;i<str.length();i++){
            for(int j=0;j<10;j++){
                if((str.charAt(i) - '0') == j){
                    ++arr[j];
                    break;
                }
            }
        }
        for(int i=0;i<10;i++){
            System.out.println(arr[i]);
        }
    }
}