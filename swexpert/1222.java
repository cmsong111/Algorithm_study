import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;

        for (int testCase = 1; testCase <= T; testCase++) {
            int size = Integer.parseInt(bf.readLine());
            List<Integer> arr = new ArrayList<>();

            st = new StringTokenizer(bf.readLine(), "+");
            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }

            System.out.printf("#%d %d\n", testCase, arr.stream().mapToInt(Integer::valueOf).sum());
        }
    }
}