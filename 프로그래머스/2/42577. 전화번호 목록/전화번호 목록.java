import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashSet<String> set = new HashSet<>(Arrays.asList(phone_book));
        //set에 phone_book의 원본 배열값 가져오기
        for(String val : set) { //val에 set값 저장 
            for(int i = 1; i<=val.length(); i++) { //1부터 val의 길이만큼 i값 1씩 증가
             
                if(set.contains(val.substring(0, i)) && val.substring(0, i).hashCode() != val.hashCode()) { //set에 해당 값이 있는지 contains로 조회 동일한 (0,i) 값을 가진 hashCode가 존재한다면 false를 return한다.
                    return false; 
                }
            }
        }

        return answer;
    }
}