class Solution {
    public int ans(int a){
    int i = 1;
    int tmp = 0;
    while(i <= a){
        if(a % i == 0){
            tmp++;
        }
       i++;
    }
    
    if(tmp > 2) return 1;
    else return 0;
}
    public int solution(int n) {
        int answer = 0;
          
    for(int i=4;i<=n;i++){
        answer += ans(i);
    }
        return answer;
    }
}