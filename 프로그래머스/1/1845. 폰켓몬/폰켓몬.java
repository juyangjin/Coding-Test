import java.util.*;

public class Solution {
  public int solution(int[] nums) {
    int max = nums.length / 2;
    HashSet<Integer> nSet = new HashSet<>();

    for (int num : nums) {
      nSet.add(num);
    }
      int answer = nSet.size() > max ? max : nSet.size();
      return answer;
  }
}