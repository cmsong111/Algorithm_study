import java.util.*;
import java.io.*;

public class Main {

	static char[] operators = {
			'+', '-', '*', '/'
	};

	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// 숫자 개수
		int N = Integer.parseInt(bf.readLine().trim());

		// 숫자 배열
		st = new StringTokenizer(bf.readLine());
		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		// 연산자 개수 4개 (+ - * /) 순서
		int[] operatorCount = new int[4];
		st = new StringTokenizer(bf.readLine());
		for (int j = 0; j < 4; j++) {
			operatorCount[j] = Integer.parseInt(st.nextToken());
		}

		// 결과 계산
		int[] result = solution(N, arr, operatorCount);

		// 결과 출력 (최댓값, 최솟값)
		System.out.println(result[0]);
		System.out.println(result[1]);
	}

	public static int[] solution(int N, int[] arr, int[] operatorCount) {
		List<char[]> operatorCombinations = backtracking(operatorCount);

		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;

		for (char[] operators : operatorCombinations) {
			int currentResult = arr[0];
			for (int i = 0; i < operators.length; i++) {
				switch (operators[i]) {
					case '+': {
						currentResult += arr[i + 1];
						break;
					}
					case '-': {
						currentResult -= arr[i + 1];
						break;
					}
					case '*': {
						currentResult *= arr[i + 1];
						break;
					}
					case '/': {
						currentResult /= arr[i + 1];
						break;
					}
				}
			}
			max = Math.max(max, currentResult);
			min = Math.min(min, currentResult);
		}

		int[] result = new int[2];
		result[0] = max;
		result[1] = min;

		return result;
	}

	/**
	 * 백트랙킹을 통해서 모든 연산자 조합을 탐색
	 *
	 * @param operatorCount 남은 연산자 개수
	 */
	private static List<char[]> backtracking(int[] operatorCount) {
		List<char[]> results = new ArrayList<>();
		int totalOperators = Arrays.stream(operatorCount).sum();
		char[] currentCombination = new char[totalOperators];

		backtrackHelper(operatorCount, currentCombination, 0, results);

		return results;
	}

	private static void backtrackHelper(int[] operatorCount, char[] currentCombination, int i, List<char[]> results) {
		if (i == currentCombination.length) {
			results.add(currentCombination.clone());
			return;
		}
		for (int j = 0; j < operators.length; j++) {
			if (operatorCount[j] > 0) {
				currentCombination[i] = operators[j];
				operatorCount[j]--;
				backtrackHelper(operatorCount, currentCombination, i + 1, results);
				operatorCount[j]++;
			}
		}
	}
}
