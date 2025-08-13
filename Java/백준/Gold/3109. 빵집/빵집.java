import java.io.*;
import java.util.*;

class Main {
	static int R, C;
	static char[][] map;
	static int answer = 0;
	static int[] dr = {-1, 0, 1};


	// dfs는 boolean을 반환하여 파이프 연결 성공 여부를 알림
	public static boolean dfs(int r, int c) {
		// 현재 위치를 방문 처리 (파이프가 놓인 것으로 간주)
		map[r][c] = '-';

		// 마지막 열에 도달했다면 성공
		if (c == C - 1) {
			return true;
		}

		// 다음 위치 탐색 (오른쪽-위, 오른쪽, 오른쪽-아래 순서)
		for (int i = 0; i < 3; i++) {
			int nr = r + dr[i];
			int nc = c + 1; // 열은 항상 1 증가

			// 1. 맵 범위를 벗어나는지 확인
			if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
				continue;
			}

			// 2. 다음 칸이 비어있는지 확인 (건물이거나 이미 파이프가 놓인 곳은 안됨)
			if (map[nr][nc] == '.') {
				// 다음 경로 탐색이 성공했다면, 즉시 true를 반환하며 재귀 종료
				if (dfs(nr, nc)) {
					return true;
				}
			}
		}

		// 3가지 방향 모두 실패했다면, 이 길은 막힌 길이므로 false 반환
		return false;
	}


	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		// 배열의 크기 N, M
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		// N * M 크기의 배열을 생성한다.
		map = new char[R][C];
		for (int i = 0; i < R; i++) {
			map[i] = br.readLine().toCharArray();
		}
		// 0번 행부터 순서대로 파이프 놓기를 시도
		for (int i = 0; i < R; i++) {
			if (dfs(i, 0)) {
				answer++;
			}
		}

		System.out.println(answer);
	}
}

