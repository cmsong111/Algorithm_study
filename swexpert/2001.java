import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int result = 0;

            // 배열 입력
            int[][] arr = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

            // 파리채 영역 브루트포스 계산
            for (int i = 0; i < N - M + 1; i++) {
                for (int j = 0; j < N - M + 1; j++) {
                    // 해당 영역 파리 사망 수 계산
                    int score = 0;
                    for (int x = i; x < i + M; x++) {
                        for (int y = j; y < j + M; y++) {
                            score += arr[x][y];
                        }
                    }

                    // 만약 전체 합보다 크다면, 결과 업데이트
                    if (result < score) {
                        result = score;
                    }
                }
            }

            // 결과 출력
            System.out.println("#" + test_case + " " + result);
        }
    }
}