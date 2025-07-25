import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = 10;

        for (int testCase = 1; testCase <= T; testCase++) {
            // 글자 길이 = N
            int N = Integer.parseInt(scanner.nextLine());
            String infix = scanner.nextLine();

            // 중위표현식을 후위표현식으로 변환
            Stack<Character> stack = new Stack<Character>();
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < N; i++) {
                switch (infix.charAt(i)) {
                    case '*':
                    case '/':
                    case '-':
                    case '+':
                        // 우선순위가 높은 연산자까지 POP!
                        while (!stack.isEmpty() && priority(stack.peek()) >= priority(infix.charAt(i))) {
                            sb.append(stack.pop());
                        }
                        stack.push(infix.charAt(i));
                        break;
                    case '(':
                        // 괄호는 최우선 연산자임
                        stack.push('(');
                        break;
                    case ')':
                        while (!stack.isEmpty() && stack.peek() != '(') {
                            sb.append(stack.pop());
                        }
                        stack.pop();
                        break;
                    default:
                        sb.append(infix.charAt(i));
                }
            }
            while (!stack.isEmpty()) {
                sb.append(stack.pop());
            }

            // 후위표현식을 계산한다
            String postFix = sb.toString();
            Stack<Integer> calStack = new Stack<Integer>();
            for (int i = 0; i < postFix.length(); i++) {
                char c = postFix.charAt(i);
                if (Character.isDigit(c)) {
                    calStack.push(c - '0');
                } else {
                    int b = calStack.pop();
                    int a = calStack.pop();
                    if (c == '+') {
                        calStack.push(a + b);
                    } else if (c == '*') {
                        calStack.push(a * b);
                    }
                }
            }
            int result = calStack.pop();
            System.out.println("#" + testCase + " " + result);
        } // TestCase 끝
    }

    /**
     * 연산자 우선순위
     *
     * @param operation 연산자
     * @return 우선순위
     */
    static int priority(char operation) {
        switch (operation) {
            case '*':
            case '/':
                return 2;
            case '-':
            case '+':
                return 1;
            default:
                return 0;
        }
    }
}
