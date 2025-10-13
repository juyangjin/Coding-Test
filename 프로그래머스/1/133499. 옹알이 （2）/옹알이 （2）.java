class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] pron = {"aya", "ye", "woo", "ma"};
        
        for(String word : babbling) {
            int i = 0;
            boolean valid = true;
            String last = ""; //연속된 단어 방지를 위한 마지막 단어 변수    
            
            while(i < word.length()){
                boolean match = false;
                        
                for(int j=0;j<pron.length;j++) {
                    if(word.startsWith(pron[j],i) && !pron[j].equals(last)){
                        last = pron[j];
                        i += pron[j].length();
                        match = true;
                        break;
                    }
                }
                if(!match){
                    valid = false;
                    break;
                }
            }
            if(valid){
            answer++; 
            }
        }
        return answer;
    }
}