import java.util.Arrays;
import java.util.Collections;

class Solution {
    public long solution(long n) {
        String[] arr = String.valueOf(n).split("");
        Arrays.sort(arr,Collections.reverseOrder());
        
        StringBuilder Buil = new StringBuilder();
		for (int i = 0; i < arr.length; i++) {
			Buil.append(arr[i]);
		}
        
        return Long.parseLong(Buil.toString());
    }
}