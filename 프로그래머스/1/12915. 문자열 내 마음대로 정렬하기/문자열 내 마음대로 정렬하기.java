import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        
        for(int i=0;i<strings.length;i++) {
            for(int j=i;j< strings.length;j++){
                char f = strings[i].charAt(n);
                char s = strings[j].charAt(n);
                if (f == s){
                    if(strings[i].compareTo(strings[j]) > 0){
                        String tmp = strings[i];
                        strings[i] = strings[j];
                        strings[j] = tmp;
                    }
                }
                else if(f > s){
                    String tmp2 = strings[i];
                    strings[i] = strings[j];
                    strings[j] = tmp2;
                }
            }
        }
        return strings;
    }
}