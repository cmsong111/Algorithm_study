import java.util.Scanner;
import java.util.Arrays;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            // 로직
            int[] arr = new int[10];
            for (int i = 0; i < 10; i++) {
                arr[i] = sc.nextInt();
            }

            // 평균 구하는 로직
            int sum = Arrays.stream(arr).sum();

            // 결과 출력
            System.out.println("#" + test_case + " " + Math.round((float) sum / 10));
        }
	}
}