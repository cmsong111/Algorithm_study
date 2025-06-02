import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		// 고속 입력
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// T: 테스트 케이스의 개수
		int T = Integer.parseInt(br.readLine());

		while (T-- > 0) {
			// N: 국가의 수
			// M: 비행기 종류
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			// 비행기 종류별? 노선
			for (int i = 0; i < M; i++) {
				br.readLine();
			}

			System.out.println(N - 1);
		}
	}
}
