class Solution {
    boolean isPrime(int n) {
    if(n==1) return false;
        for(int i=2; i*i<=n;i++){
            if(n%i==0) return false;
        }  
        // System.out.println("n은" + n);
        return true;
    }
    
    public int solution(int[] nums) {
        int answer = 0;
        int num = 0;

        for(int i=0;i<nums.length;i++) {
            for(int j=i+1;j<nums.length;j++){
                for(int z=j+1;z<nums.length;z++){
                    num = nums[i] + nums[j] + nums[z];
                    // System.out.println("첫번째 숫자 " + nums[i] + "두번째 숫자 " + nums[j] + "세번째 숫자 " + nums[z]);
                    // System.out.println("num은" + num);
                    if(isPrime(num)){
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}