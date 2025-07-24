import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Solution {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int T = 10;

		/** 연산자 우선순위 */
		Map<String, Integer> priority = new HashMap<>();
		priority.put("*", 2);
		priority.put("+", 1);

		for (int testCase = 1; testCase <= T; testCase++) {
			// 글자 길이 = N
			int N = Integer.parseInt(scanner.nextLine());
			String infix = scanner.nextLine();

			// 후위표기법으로 변환하기 위한 스택
			StringBuilder postfix = new StringBuilder();
			Stack<Character> stack = new Stack<>();

			for (int i = 0; i < N; i++) {
				// 중위표기법을 후위표기법으로 변환
				char c = infix.charAt(i);
				if (Character.isDigit(c)) {
					// 숫자면 바로 출력
					postfix.append(c);
				} else {
					// 연산자면 우선순위에 따라 처리
					while (!stack.isEmpty() && priority.get(String.valueOf(c)) <= priority.get(String.valueOf(stack.peek()))) {
						postfix.append(stack.pop());
					}
					stack.push(c);
				}
			}
			// 스택에 남아있는 연산자들을 모두 출력
			while (!stack.isEmpty()) {
				postfix.append(stack.pop());
			}

			// 후위표기법을 이용해 계산
			Stack<Integer> calcStack = new Stack<>();
			for (int i = 0; i < postfix.length(); i++) {
				char c = postfix.charAt(i);
				if (Character.isDigit(c)) {
					// 숫자면 스택에 넣기
					calcStack.push(c - '0');
				} else {
					// 연산자면 스택에서 두 개의 숫자를 꺼내서 계산 후 다시 스택에 넣기
					int b = calcStack.pop();
					int a = calcStack.pop();
					if (c == '+') {
						calcStack.push(a + b);
					} else if (c == '*') {
						calcStack.push(a * b);
					}
				}
			}
			// 계산 결과 출력
			int result = calcStack.pop();
			System.out.printf("#%d %d\n", testCase, result);
		}
	}
}
