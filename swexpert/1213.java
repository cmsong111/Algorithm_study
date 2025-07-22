import java.util.Scanner;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            bf.readLine();
            String target = bf.readLine();
            String str = bf.readLine();

            int result = 0;
            // 문자열 비교
            for (int i = 0; i <= str.length() - target.length(); i++) {
                if (str.startsWith(target, i)) {
                    result++;
                }
            }
            
            System.out.printf("#%d %d\n", testCase, result);
        }
    }
}