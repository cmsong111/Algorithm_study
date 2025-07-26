import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;

        for (int testCase = 1; testCase <= T; testCase++) {
            // 입력
            bf.readLine();
            int[][] table = new int[100][100];
            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < 100; j++) {
                    table[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 알고리즘 처리
            // 열 기준으로 내려가면서 0 은 스킵, 12 갯수만 찾으면 교착상태를 찾을 수 있음
            int result = 0;
            for (int i = 0; i < 100; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < 100; j++) {
                    if (table[j][i] != 0) {
                        sb.append(table[j][i]);
                    }
                }
                result += countOccurrences(sb.toString(), "12");
            }

            System.out.printf("#%d %d\n", testCase, result);
        }
    }

    public static int countOccurrences(String str, String target) {
        int count = 0;
        for (int i = 0; i <= str.length() - target.length(); i++) {
            if (str.startsWith(target, i)) {
                count++;
            }
        }
        return count;
    }
}