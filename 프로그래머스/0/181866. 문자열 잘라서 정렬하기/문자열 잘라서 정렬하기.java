import java.util.*;
import java.io.*;

class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x");
        ArrayList<String> result = new ArrayList<>();
        
        for (String str : answer) {
            if (!str.isEmpty()) {
                result.add(str);
            }
        }
        
        String[] Arr = result.toArray(new String[result.size()]);
        Arrays.sort(Arr);
        
        return Arr;
    }
}