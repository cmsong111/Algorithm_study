import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		// 총 스위치 개수
		int N = Integer.parseInt(br.readLine());

		// 스위치 상태
		int[] swoitches = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			swoitches[i] = Integer.parseInt(st.nextToken());
		}

		// 스위치 조작 횟수
		int M = Integer.parseInt(br.readLine());
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			// 성별 1: 남자, 2: 여자
			int gender = Integer.parseInt(st.nextToken());
			int num = Integer.parseInt(st.nextToken());

			if (gender == 1) {
				// 남자인 경우
				// num의 배수 스위치 상태 변경
				for (int j = num -1; j < N; j += num) {
					if (swoitches[j] == 0) {
						swoitches[j] = 1;
					} else {
						swoitches[j] = 0;
					}
				}
			} else {
				// 여자인 경우
				// num을 기준으로 좌우 대칭으로 스위치 상태 변경
				// 좌측
				int left = num;
				int right = num;
				while (left > 0 && right <= N) {
					if (swoitches[left - 1] == swoitches[right - 1]) {
						if (swoitches[left - 1] == 0) {
							swoitches[left - 1] = 1;
							swoitches[right - 1] = 1;
						} else {
							swoitches[left - 1] = 0;
							swoitches[right - 1] = 0;
						}
					} else {
						break;
					}
					left--;
					right++;
				}
			}
		}

		// 스위치 상태 출력
		for (int i = 0; i < N; i++) {
			System.out.print(swoitches[i] + " ");
			if ((i + 1) % 20 == 0) {
				System.out.println();
			}
		}
	}
}
