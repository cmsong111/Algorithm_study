import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
	
			int answer = 0;

            // 10개의 숫자 더하기
            for (int i = 0; i < 10; i++) {
                int num = sc.nextInt();

                if (num % 2 == 1) {
                    answer += num;
                }
            }

            System.out.println("#" + test_case + " " + answer);
		}
	}
}