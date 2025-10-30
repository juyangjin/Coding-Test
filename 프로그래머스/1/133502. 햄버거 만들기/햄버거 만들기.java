import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        List<Integer> ing = new ArrayList<>();
        List<Integer> pattern = Arrays.asList(1, 2, 3, 1);
        int count = 0;
        int ps = pattern.size();
        
        for(int i:ingredient) {
            ing.add(i); 
            int size = ing.size();
            
            if(size >=ps && ing.subList(size-ps, size).equals(pattern)) {
                for(int j=0; j<4; j++) ing.remove(ing.size()-1);
                count++;
            }
        }
        return count;
    }
}