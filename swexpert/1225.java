import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            // 입력
            int tc = Integer.parseInt(bf.readLine());
            st = new StringTokenizer(bf.readLine());
            Deque<Integer> deque = new ArrayDeque<>();
            while (st.hasMoreTokens()) {
                deque.add(Integer.parseInt(st.nextToken()));
            }

            xx:
            while (true) {
                for (int i = 1; i <= 5; i++) {
                    deque.addLast(
                            deque.pollFirst() - i
                    );
                    if (deque.peekLast() <= 0) {
                        break xx;
                    }
                }
            }

            System.out.print("#" + tc + " ");
            for (int i = 0; i < 7; i++) {
                System.out.print(deque.pollFirst() + " ");
            }
            System.out.println("0");
        } // TestCase 끝
    }
}
