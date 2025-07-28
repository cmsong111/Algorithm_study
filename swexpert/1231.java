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
            // 입력
            int N = Integer.parseInt(bf.readLine());
            Node[] nodes = new Node[N];
            for (int i = 0; i < N; i++) {
                nodes[i] = new Node();
            }

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(bf.readLine());
                st.nextToken();
                Character value = st.nextToken().charAt(0);
                Node left = st.hasMoreTokens() ? nodes[Integer.parseInt(st.nextToken()) - 1] : null;
                Node right = st.hasMoreTokens() ? nodes[Integer.parseInt(st.nextToken()) - 1] : null;
                nodes[i].update(value, left, right);
            }

            // 중위순회
            System.out.printf("#%d ", testCase);
            preOrder(nodes[0]);
            System.out.println("");
        } // TestCase 끝
    }

    public static void preOrder(Node node) {
        if (node != null) {
            if (node.left != null) preOrder(node.left);
            System.out.print(node.value);
            if (node.right != null) preOrder(node.right);
        }
    }

    static class Node {
        public Character value;
        public Node left;
        public Node right;

        public Node() {

        }

        public void update(Character value, Node left, Node right) {
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }
}
