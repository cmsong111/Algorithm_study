import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = 10;

        for (int testCase = 1; testCase <= T; testCase++) {
            sc.nextInt();
            int N = sc.nextInt();
            int M = sc.nextInt();

            System.out.printf("#%d %d\n", testCase, pow(N, M));
        }
    }

    // 재귀함수
    public static int pow(int num, int pow) {
        if (pow == 0) return 1;
        if (pow == 1) return num;
        return num * pow(num, pow - 1);
    }
}