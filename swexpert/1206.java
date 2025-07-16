import java.util.Scanner;
import java.util.Arrays;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            // 빌딩 갯수
            int N = sc.nextInt();
            sc.nextLine(); // 개행제거

            // 빌딩 입력
            int[] buildings = new int[N];
            for (int i = 0; i < N; i++) {
                buildings[i] = sc.nextInt();
            }
            sc.nextLine(); // 개행 제거

            // 메인 로직
            int result = 0;

            // 중반 여러개 (0개 ~ 996개)
            // 양끝 2개씩은 항상 0 이기 때문에, 신경쓰지 않아도 된다
            for (int i = 2; i < N - 2; i++) {
                int[] side = {buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]};
                int maxSide = Arrays.stream(side).max().getAsInt();
                result += Math.max(0, buildings[i] - maxSide);
            }

            System.out.println("#" + test_case + " " + result);
		}
	}
}