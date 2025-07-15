import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.io.FileInputStream;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

        Map<String, Integer> table = new HashMap<>();
        table.put("0001101", 0);
        table.put("0011001", 1);
        table.put("0010011", 2);
        table.put("0111101", 3);
        table.put("0100011", 4);
        table.put("0110001", 5);
        table.put("0101111", 6);
        table.put("0111011", 7);
        table.put("0110111", 8);
        table.put("0001011", 9);

        for (int test_case = 1; test_case <= T; test_case++) {
            // 로직
            int N = sc.nextInt();
            int M = sc.nextInt();
            sc.nextLine(); // 개행기호 삭제
            // System.out.println("N: " + N + "\tM: " + M);

            int[] values = new int[8];

            // 유효 바코드 입력 위치 검색
            String barcode = "";
            for (int i = 0; i < N; i++) {
                String temp = sc.nextLine();
                if (temp.contains("1") && barcode.isEmpty()) {
                    barcode = temp;
                }
            }

            // 첫번째 위치 검색
            int startIndex = barcode.lastIndexOf("1") - 56 + 1;
            // System.out.println("start index: " + startIndex);

            // 바코드 입력 값 추출
            for (int i = 0; i < 8; i++) {
                String value = barcode.substring(startIndex + (i * 7), startIndex + (i * 7) + 7);
                // System.out.print(value);
                values[i] = table.get(value);
                // System.out.println(" " + table.get(value));
            }
            int checkNum = (values[0] + values[2] + values[4] + values[6]) * 3 + values[1] + values[3] + values[5] + values[7];

            if (checkNum % 10 == 0) {
                System.out.println("#" + test_case + " " + Arrays.stream(values).sum());
            } else {
                System.out.println("#" + test_case + " 0");
            }

        }
    }
}