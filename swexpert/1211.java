import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = 10;
        for (int testCase = 1; testCase <= T; testCase++) {
            // 테스트케이스 입력
            bf.readLine();

            int[][] map = new int[100][100];
            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(bf.readLine());
                for (int j = 0; j < 100; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 로직 스타트
            // Map <출발지,이동거리>
            Map<Integer, Integer> results = new HashMap<>();

            // X열 이동
            for (int i = 0; i < 100; i++) {
                if (map[0][i] == 0) {
                    // 길이없다면 패스
                    continue;
                }

                int currentXPosition = i;
                int distance = 0;

                // Y축 내려감
                for (int j = 0; j < 100; j++) {
                    if (currentXPosition > 0 && map[j][currentXPosition - 1] == 1) {
                        while (currentXPosition > 0 && map[j][currentXPosition - 1] == 1) {
                            currentXPosition--;
                            distance++;
                        }
                    } else if (currentXPosition < 99 && map[j][currentXPosition + 1] == 1) {
                        while (currentXPosition < 99 && map[j][currentXPosition + 1] == 1) {
                            currentXPosition++;
                            distance++;
                        }
                    }
                    distance++;
                }

                results.put(i, distance);
            }

            // 결과 출력
            Map.Entry<Integer, Integer> result = new AbstractMap.SimpleEntry<>(-1, Integer.MAX_VALUE);
            for (Map.Entry<Integer, Integer> entry : results.entrySet()) {
                if (result.getValue() > entry.getValue()) {
                    result = entry;
                }
            }

            System.out.printf("#%d %d\n", testCase, result.getKey());
        }
    }
}