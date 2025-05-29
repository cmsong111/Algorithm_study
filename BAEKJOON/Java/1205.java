import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		// 고속 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// P: 랭킹 리스트에 올라 갈 수 있는 점수의 개수
		// score: 태수의 점수
		// N: 리스트에 있는 점수
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int score = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());

		// 랭킹 리스트에 올라갈 수 있는 점수의 개수가 0인 경우
		if (N == 0) {
			System.out.println(1);
			return;
		}

		// 랭킹 리스트에 있는 점수
		int[] ranking = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			ranking[i] = Integer.parseInt(st.nextToken());
		}

		// 내 점수 이상인 점수 개수
		int count = 0;
		// 내 점수와 같은 점수의 개수
		int sameScoreCount = 0;

		// 랭킹 리스트에 있는 점수와 비교
		for (int i = 0; i < N; i++) {
			if (ranking[i] > score) {
				count++;
			} else if (ranking[i] == score) {
				sameScoreCount++;
			}
		}

		// 랭킹 리스트에 올라갈 수 있는지 여부
		if (P >= sameScoreCount + count + 1) {
			System.out.println(count + 1);
		} else {
			System.out.println(-1);
		}
	}
}
