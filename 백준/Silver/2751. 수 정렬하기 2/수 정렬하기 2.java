import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i=0;i<n;i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(arr);
        
		for(Object sum : arr){
            System.out.println(sum);
        }
    }
}