import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCases = Integer.parseInt(br.readLine());
        // 테스트 케이스
        for (int tc = 0; tc < testCases; tc++) {
            // N 입력
            int n = Integer.parseInt(br.readLine());
            int[] upLine = new int[n];
            int[] downLine = new int[n];

            // Up, down 입력
            String[] upLineStr = br.readLine().split(" ");
            String[] downLineStr = br.readLine().split(" ");

            for (int i = 0; i < n; i++) {
                upLine[i] = Integer.parseInt(upLineStr[i]);
                downLine[i] = Integer.parseInt(downLineStr[i]);
            }
            // n이 1일 때 예외처리
            if (n == 1) {
                System.out.println(Math.max(upLine[0], downLine[0]));
                continue;
            }
            // n이 2일 때 예외처리
            else if (n == 2) {
                System.out.println(Math.max(upLine[0] + downLine[1], upLine[1] + downLine[0]));
                continue;
            }

            // dp 배열 2번 세팅
            upLine[1] += downLine[0];
            downLine[1] += upLine[0];

            // DP 뱅글뱅글 돌리기
            for (int i = 2; i < n; i++) {
                upLine[i] += Math.max(downLine[i - 1], downLine[i - 2]);
                downLine[i] += Math.max(upLine[i - 1], upLine[i - 2]);
            }

            // 정답 출력
            System.out.println(Math.max(upLine[n - 1], downLine[n - 1]));
        }
    }
}
