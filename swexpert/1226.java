import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {

	private static final int SIZE = 16;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		int T = 10;
		for (int testCase = 1; testCase <= T; testCase++) {
			int testCaseNumber = Integer.parseInt(bf.readLine());
			char[][] map = new char[SIZE][SIZE];
			for (int i = 0; i < SIZE; i++) {
				String line = bf.readLine();
				map[i] = line.toCharArray();
			}


			// 2 : 시작점
			// 3 : 도착점
			Point start = null;
			Point end = null;

			for (int i = 0; i < SIZE; i++) {
				for (int j = 0; j < SIZE; j++) {
					if (map[i][j] == '2') {
						start = new Point(i, j);
					} else if (map[i][j] == '3') {
						end = new Point(i, j);
					}
				}
			}

			// BFS 로직으로 2에서 3으로 갈 수 있는지 확인
			boolean[][] visited = new boolean[SIZE][SIZE];
			Deque<Point> stack = new ArrayDeque<>();
			int[] dx = {0, 0, -1, 1}; // 상하좌우
			int[] dy = {-1, 1, 0, 0};

			stack.push(start);
			visited[start.x][start.y] = true;

			boolean found = false;

			while (!stack.isEmpty()) {
				Point current = stack.pop();
				if (current.x == end.x && current.y == end.y) {
					found = true;
					break;
				}

				for (int i = 0; i < 4; i++) {
					int nx = current.x + dx[i];
					int ny = current.y + dy[i];

					if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE && !visited[nx][ny] && map[nx][ny] != '1') {
						visited[nx][ny] = true;
						stack.push(new Point(nx, ny));
					}
				}
			}

			System.out.println("#" + testCaseNumber + " " + (found ? 1 : 0));
		}
	}

	static class Point {
		int x;
		int y;

		Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}

