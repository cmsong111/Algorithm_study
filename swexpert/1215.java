import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            // 입력
            int size = Integer.parseInt(bf.readLine());
            char[][] board = new char[8][8];
            for (int i = 0; i < 8; i++) {
                st = new StringTokenizer(bf.readLine(), "");
                board[i] = st.nextToken().toCharArray();
            }

            // 로직 처리
            int result = 0;

            // 가로 비교
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8 - size +1; j++) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < size; k++) {
                        sb.append(board[i][j + k]);
                    }
                    String str = sb.toString();
                    String strReverse = sb.reverse().toString();
                    if (str.equals(strReverse)) {
                        result++;
                    }
                }
            }

            // 세로 비교
            for (int i = 0; i < 8 - size +1; i++) {
                for (int j = 0; j < 8; j++) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < size; k++) {
                        sb.append(board[i + k][j]);
                    }
                    String str = sb.toString();
                    String strReverse = sb.reverse().toString();
                    if (str.equals(strReverse)) {
                        result++;
                    }
                }
            }
            System.out.printf("#%d %d\n", testCase, result);
        }
    }
}