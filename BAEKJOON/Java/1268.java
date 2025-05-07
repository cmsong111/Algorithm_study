import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		// 학생 수
		int N = Integer.parseInt(br.readLine());

		// 1학년부터 5학년까지 반 정보를 저장할 배열
		int[][] arr = new int[N][5];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}



		//1학년부터 5학년까지 같은반 친구가 존재하면 친구를 Set에 저장
		List<Set<Integer>> list = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			list.add(new HashSet<>());
		}

		// 1학년부터 5학년까지 같은 반 친구를 찾기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				for (int k = 0; k < 5; k++) {
					if (arr[i][k] == arr[j][k]) {
						list.get(i).add(j);
						break;
					}
				}
			}
		}

		// 각 학생의 친구 수를 세기
		int max_size = 1;
		int max_index = 1;

		for (int i = 0; i < N; i++) {
			int size = list.get(i).size();
			if (size > max_size) {
				max_size = size;
				max_index = i + 1;
			}
		}

		System.out.println(max_index);

	}
}
