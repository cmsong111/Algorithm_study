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
            int N = Integer.parseInt(bf.readLine());
            ArrayList<Integer> arr = new ArrayList<>();
            st = new StringTokenizer(bf.readLine());
            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }

            int M = Integer.parseInt(bf.readLine());
            st = new StringTokenizer(bf.readLine());
            for (int i = 0; i < M; i++) {
                Character operator = st.nextToken().charAt(0);
                switch (operator) {
                    case 'I': {
                        // 1. I(삽입) x, y, s : 앞에서부터 x번째 암호문 바로 다음에 y개의 암호문을 삽입한다. s는 덧붙일 암호문들이다.[ ex) I 3 2 123152 487651 ]
                        Integer index = Integer.parseInt(st.nextToken());
                        Integer moreArrLen = Integer.parseInt(st.nextToken());
                        ArrayList<Integer> moreArr = new ArrayList<>();
                        for (int j = 0; j < moreArrLen; j++) {
                            moreArr.add(Integer.parseInt(st.nextToken()));
                        }
                        arr.addAll(index, moreArr);
                        break;
                    }
                    case 'D': {
                        // 2. D(삭제) x, y : 앞에서부터 x번째 암호문 바로 다음부터 y개의 암호문을 삭제한다.[ ex) D 4 4 ]
                        Integer x = Integer.parseInt(st.nextToken());
                        Integer y = Integer.parseInt(st.nextToken());
                        for (int j = 0; j < y; j++) {
                            arr.remove(x);
                        }
                        break;
                    }

                    case 'A': {
                        // 3. A(추가) y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다. s는 덧붙일 암호문들이다. [ ex) A 2 421257 796813 ]
                        int y = Integer.parseInt(st.nextToken());
                        for (int j = 0; j < y; j++) {
                            arr.add(Integer.parseInt(st.nextToken()));
                        }
                        break;
                    }

                }

            }

            System.out.print("#" + testCase + " ");
            for (int i = 0; i < 10; i++) {
                System.out.print(arr.get(i) + " ");
            }
            System.out.println(" ");
        } // TestCase 끝
    }
}
