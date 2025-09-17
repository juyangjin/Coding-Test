class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int j = 0;
        int z = 0;
        
        for (String word : goal) { 
            if(j<cards1.length && word.equals(cards1[j])){
                j++;
            } else if(z<cards2.length && word.equals(cards2[z])){
                z++;
            } else {
                    return "No";
            }
        }
        return "Yes";
    }
}