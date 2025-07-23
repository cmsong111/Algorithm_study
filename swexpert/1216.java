import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int SIZE = 100;

        int T = 10;
        for (int tc = 1; tc <= T; tc++) {
            // 입력
            int testCase = Integer.parseInt(bf.readLine());
            char[][] board = new char[SIZE][SIZE];
            for (int i = 0; i < SIZE; i++) {
                st = new StringTokenizer(bf.readLine(), "");
                board[i] = st.nextToken().toCharArray();
            }

            // 로직 처리
            int result = 0;

            // 가로 비교
            for (int i = 0; i < SIZE; i++) {
                for (int j = 0; j < SIZE; j++) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = j; k < SIZE; k++) {
                        sb.append(board[i][k]);
                        String str = sb.toString();
                        String strReverse = sb.reverse().toString();
                        if (str.equals(strReverse) && result < str.length()) {
                            result = str.length();
                        }
                        sb.reverse();
                    }
                }
            }


            // 세로 비교
            for (int i = 0; i < SIZE; i++) {
                for (int j = 0; j < SIZE; j++) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = i; k < SIZE; k++) {
                        sb.append(board[k][j]);
                        String str = sb.toString();
                        String strReverse = sb.reverse().toString();
                        if (str.equals(strReverse) && result < str.length()) {
                            result = str.length();
                        }
                        sb.reverse();
                    }
                }
            }
            System.out.printf("#%d %d\n", testCase, result);
        }
    }
}