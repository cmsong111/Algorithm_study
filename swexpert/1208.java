import java.util.*;
import java.io.FileInputStream;


class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = 10;

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int dumpCount = sc.nextInt();


            // 영역 입력 힙을 이용해서 빠르게 정렬하기
            ArrayList<Integer> area = new ArrayList<Integer>();
            for (int i = 0; i < 100; i++) {
                area.add(sc.nextInt());
            }

            // 덤프 횟수에 맞게 덤프 트럭 사용하기
            for (int i = 0; i < dumpCount; i++) {
                area.sort(((o1, o2) -> o1 - o2));

                area.set(0, area.get(0) + 1);
                area.set(99, area.get(99) - 1);
            }
            area.sort(((o1, o2) -> o1 - o2));

            // 높이 차이 계산
            System.out.println("#" + test_case + " " + (area.get(99) - area.get(0)));
        }
    }
}