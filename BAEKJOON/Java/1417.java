import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int target = sc.nextInt();
		int result = 0;

		// 우선순위 큐
		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
		for (int i = 1; i < N; i++) {
			pq.add(sc.nextInt());
		}

		while (!pq.isEmpty() && target <= pq.peek()) {
			int cur = pq.poll();
			cur--;
			target++;
			result++;
			pq.add(cur);
		}

		System.out.println(result);
	}
}
