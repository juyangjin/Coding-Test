import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader bf =
            new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer sTr = 
            new StringTokenizer(bf.readLine());
        
        int suNo = Integer.parseInt(sTr.nextToken());
        int quizNo = Integer.parseInt(sTr.nextToken());
       
        long[] S = new long[suNo+1];
        sTr = new StringTokenizer(bf.readLine());
        for(int i=1;i<=suNo;i++){
            S[i] = S[i-1] + Integer.parseInt(sTr.nextToken());
        }
        for(int q=0;q<quizNo;q++){
            sTr = new StringTokenizer(bf.readLine());
            int i = Integer.parseInt(sTr.nextToken());
            int j = Integer.parseInt(sTr.nextToken());
            System.out.println(S[j] - S[i-1]);
        }
    }
}