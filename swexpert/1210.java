import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = 10;

        for (int test_case = 1; test_case <= T; test_case++) {
            // 테스트케이스 번호 입력
            sc.nextInt();

            // 보드 입력
            int[][] board = new int[100][100];
            for (int y = 0; y < 100; y++) {
                for (int x = 0; x < 100; x++) {
                    board[x][y] = sc.nextInt();
                }
            }

            // 출발점 검색 (2)
            int pos_x = Integer.MAX_VALUE, pos_y = 99;
            for (int x = 0; x < 100; x++) {
                if (board[x][pos_y] == 2) {
                    pos_x = x;
                    break;
                }
            }

            // 스텝별로 이동하면서, 좌측,우측이 1이면 0이 나올때까지 이동하기
            while (pos_y != 0) {
//                System.out.println("TestCase:" + test_case + " Posision: " + pos_x + "," + pos_y + " value: " + board[pos_x][pos_y]);
                // 왼쪽 처리
                if (0 < pos_x && board[pos_x - 1][pos_y] == 1) {
//                    System.out.println("왼쪽으로 감 to : x: " + (pos_x - 1) + "\ty: " + pos_y + ":" + board[pos_x - 1][pos_y]);
                    while (0 < pos_x && board[pos_x - 1][pos_y] == 1) {
                        pos_x--;
                    }
                }
                // 우측 처리
                else if (pos_x < 99 && board[pos_x + 1][pos_y] == 1) {
//                    System.out.println("우측으로 감");
                    while (pos_x < 99 && board[pos_x + 1][pos_y] == 1) {
                        pos_x++;
                    }
                }
                // 직진~
                pos_y--;
            }

            System.out.println("#" + test_case + " " + pos_x);
//            System.out.println();
        }
    }
}