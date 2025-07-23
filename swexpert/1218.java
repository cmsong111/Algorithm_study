import java.util.Scanner;
import java.util.Stack;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = 10;

        for (int testCase = 1; testCase <= T; testCase++) {
            sc.nextLine();
            String str = sc.nextLine();

            Stack<Character> stack = new Stack<>();
            boolean result = true;

            for (char c : str.toCharArray()) {
                if (c == '[' || c == '{' || c == '('|| c == '<') {
                    stack.push(c);
                } else if (c == ']' && stack.peek() == '[') {
                    stack.pop();
                } else if (c == '}' && stack.peek() == '{') {
                    stack.pop();
                } else if (c == ')' && stack.peek() == '(') {
                    stack.pop();
                } else if (c == '>' && stack.peek() == '<') {
                    stack.pop();
                } else {
                    result = false;
                    break;
                }
            }

            System.out.printf("#%d %d\n", testCase, result ? 1 : 0);
        }
    }
}