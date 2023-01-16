import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        // DP 배열 생성
        int[] left = new int[count];
        int[] right = new int[count];

        // DP 배열 초기화 & 첫번째 값 생성
        if (Integer.parseInt(st.nextToken()) == 1) {
            left[0] = 1;
            right[0] = 0;
        } else {
            left[0] = 0;
            right[0] = 1;
        }

        // DP 뱅글뱅글 돌리기
        for (int i = 1; i < count; i++) {
            if (Integer.parseInt(st.nextToken()) == 1) {
                left[i] = left[i - 1] + 1;
                right[i] = Math.max(right[i - 1] - 1, 0);
            } else {
                left[i] = Math.max(left[i - 1] - 1, 0);
                right[i] = right[i - 1] + 1;
            }
        }

        // 최대값 구하기
        int max = 0, min = 0;
        for (int i = 0; i < count; i++) {
            if (left[i] > max) {
                max = left[i];
            }
            if (right[i] > min) {
                min = right[i];
            }
        }

        // 결과 출력
        System.out.println(Math.max(min, max));
    }
}
