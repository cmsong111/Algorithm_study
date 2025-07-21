import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		        int N = sc.nextInt();

        // 369 하는데, 1개 나오면 - 2개 나오면 -- 3개 나오면 ---
        for (int i = 1; i <= N; i++) {
            String str = Integer.toString(i);
            int cnt = 0;


            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '3' || str.charAt(j) == '6' || str.charAt(j) == '9') {
                    cnt++;
                }
            }

            if (cnt == 0) {
                System.out.print(i + " ");
            } else {
                for (int j = 0; j < cnt; j++) {
                    System.out.print("-");
                }
                System.out.print(" ");
            }
        }
    }
}
