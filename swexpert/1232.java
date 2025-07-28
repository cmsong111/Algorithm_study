import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            int N = Integer.parseInt(bf.readLine());
            Node[] nodes = new Node[N];
            for (int i = 0; i < N; i++) {
                nodes[i] = new Node();
            }

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(bf.readLine());
                st.nextToken();
                String value = st.nextToken();
                Node left = st.hasMoreTokens() ? nodes[Integer.parseInt(st.nextToken()) - 1] : null;
                Node right = st.hasMoreTokens() ? nodes[Integer.parseInt(st.nextToken()) - 1] : null;
                nodes[i].update(value, left, right);
            }

            int result = excute(nodes[0]);

            System.out.printf("#%d %d\n", testCase, result);

        } // TestCase 반복문 끝
    }

    public static int excute(Node node) {
        if (node.left == null && node.right == null) {
            return Integer.parseInt(node.value);
        }

        int leftval = excute(node.left);
        int rightval = excute(node.right);

        switch (node.value) {
            case "+":
                return leftval + rightval;
            case "-":
                return leftval - rightval;
            case "/":
                return leftval / rightval;
            case "*":
                return leftval * rightval;
            default:
                throw new IllegalArgumentException("님 실수함");
        }
    }

    static class Node {
        String value;
        Node left;
        Node right;

        public Node() {
            value = null;
            left = null;
            right = null;
        }

        public void update(String value, Node left, Node right) {
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }
}
