import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(bf.readLine());
		Integer[] arrA = new Integer[N];
		st = new StringTokenizer(bf.readLine());
		for (int i = 0; i < N; i++) {
			arrA[i] = Integer.parseInt(st.nextToken());
		}
		Integer[] arrB = new Integer[N];
		st = new StringTokenizer(bf.readLine());
		for (int i = 0; i < N; i++) {
			arrB[i] = Integer.parseInt(st.nextToken());
		}

		int result = solution(N, arrA, arrB);
		System.out.println(result);
	}

	public static int solution(int n, Integer[] arrA, Integer[] arrB) {
		int result = 0;

		Arrays.sort(arrA);
		Arrays.sort(arrB, ((o1, o2) -> o2 - o1));

		for (int i = 0; i < n; i++) {
			result += arrA[i] * arrB[i];
		}

		return result;
	}
}
