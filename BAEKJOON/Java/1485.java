import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		// 고속 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			Position[] positions = new Position[4];

			// 입력 받기
			for (int i = 0; i < 4; i++) {
				String[] input = br.readLine().split(" ");
				int x = Integer.parseInt(input[0]);
				int y = Integer.parseInt(input[1]);
				positions[i] = new Position(x, y);
			}

			// 정사각형 판별 로직
			boolean isSquare = true;
			Double[] distances = new Double[6];
			int index = 0;
			for (int i = 0; i < 4; i++) {
				for (int j = i + 1; j < 4; j++) {
					distances[index++] = positions[i].distanceTo(positions[j]);
				}
			}

			Arrays.sort(distances);

			// 정사각형의 경우, 4개의 변의 길이가 같고, 2개의 대각선의 길이가 같아야 함
			for (int i = 0; i < 4; i++) {
				if (distances[i].compareTo(distances[0]) != 0) {
					isSquare = false;
					break;
				}
			}

			if (isSquare && distances[4].compareTo(distances[5]) != 0) {
				isSquare = false;
			}

			// 결과 출력
			System.out.println(isSquare ? 1 : 0);
		}
	}

	static class Position {
		int x, y;

		public Position(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public Double distanceTo(Position other) {
			return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
		}
	}
}
