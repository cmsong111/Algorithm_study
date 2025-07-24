import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static final int MAX_NODE = 100;
    static boolean[] visited = new boolean[MAX_NODE];


    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            // 입력
            st = new StringTokenizer(bf.readLine());
            int tc = Integer.parseInt(st.nextToken());
            int nodeLen = Integer.parseInt(st.nextToken());

            Node[] nodes = new Node[MAX_NODE];
            for (int i = 0; i < MAX_NODE; i++) {
                nodes[i] = new Node();
            }

            st = new StringTokenizer(bf.readLine());
            for (int i = 0; i < nodeLen; i++) {
                int start = Integer.parseInt(st.nextToken());
                int des = Integer.parseInt(st.nextToken());
                nodes[start].addDes(des);
            }

            // 알고리즘
            visited = new boolean[MAX_NODE];
            dfs(nodes, 0); // 0에서 출발


            // 결과 출력
            System.out.printf("#%d %d\n", testCase, visited[99] ? 1 : 0);
        }
    }

    static void dfs(Node[] nodes, int current) {
        visited[current] = true;

        if (nodes[current].left != null && !visited[nodes[current].left]) {
            dfs(nodes, nodes[current].left);
        }

        if (nodes[current].right != null && !visited[nodes[current].right]) {
            dfs(nodes, nodes[current].right);
        }
    }

    static class Node {
        Integer left = null;
        Integer right = null;

        public void addDes(int des) {
            if (left == null) {
                left = des;
            } else if (right == null) {
                right = des;
            } else {
                throw new RuntimeException("간선이 2개를 초과합니다.");
            }
        }
    }
}