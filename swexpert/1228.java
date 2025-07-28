import java.util.*;
import java.io.*;

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
                Integer index = Integer.parseInt(st.nextToken());
                Integer moreArrLen = Integer.parseInt(st.nextToken());
                ArrayList<Integer> moreArr = new ArrayList<>();
                for (int j = 0; j < moreArrLen; j++) {
                    moreArr.add(Integer.parseInt(st.nextToken()));
                }

                arr.addAll(index, moreArr);
            }

            System.out.print("#" + testCase + " ");
            for (int i = 0; i < 10; i++) {
                System.out.print(arr.get(i) + " ");
            }
            System.out.println(" ");
        } // TestCase 끝
    }
}
