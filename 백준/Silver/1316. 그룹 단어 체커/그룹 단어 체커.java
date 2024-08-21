import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    static BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
    
     public static boolean check() throws IOException { //그룹단어 체커
     boolean[] check = new boolean[26];
     int tmp = 0;
     String str = br.readLine();
     
     for(int i=0;i<str.length();i++){
         int now = str.charAt(i);
         
         if(tmp != now){
             if(check[now - 'a'] == false){
                 check[now - 'a'] = true;
                 tmp = now;
             }
             else {
                 return false;
             }
         }else{
             continue;
         }
     }
     return true;
    }
    
    public static void main(String[] args) throws IOException {
    int n = Integer.parseInt(br.readLine());
    int cnt = 0;
    
    for(int i=0;i<n;i++){
        if(check() == true){
            cnt++;
        }
    }
    System.out.print(cnt);
    }
}