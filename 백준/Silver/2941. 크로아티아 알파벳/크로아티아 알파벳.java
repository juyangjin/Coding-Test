import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        String[] cro = {"c=","c-","dz=","d-","lj","nj","s=","z="};
        String n = br.readLine();
        int idx = 0;
        for(int i=0;i<cro.length;i++){
            idx = n.indexOf(cro[i]); //크로아티아 알파벳에 해당하는 인덱스를 idx에 저장
            if(idx >= 0){
                n = n.replaceAll(cro[i],"T"); //크로아티아 알파벳 자리에 한 글자 T 저장
            }
        }
        System.out.println(n.length());
    }
}