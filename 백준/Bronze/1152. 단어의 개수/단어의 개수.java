import java.util.Scanner;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = 
            new StringTokenizer(sc.nextLine());
        int c = st.countTokens();
        System.out.print(c);
    }

}

// Scanner만 쓰인 버전 StringTokenizer는 빠르지만 레거시한 코드라서 주의.
// import java.util.*;

// public class Main {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         String s = sc.nextLine().trim(); // 앞뒤 공백 제거

//         if (s.isEmpty()) { // 문자열이 공백뿐인 경우
//             System.out.println(0);
//         } else {
//             String[] words = s.split(" "); // 공백 1개로만 구분
//             System.out.println(words.length);
//         }
//     }
// }
