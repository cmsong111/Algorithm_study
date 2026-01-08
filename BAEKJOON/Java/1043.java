
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	static int[] parent;

	static void union(int o1, int o2) {
		int a = find(o1);
		int b = find(o2);
		if (a > b) {
			parent[a] = b;
		} else {
			parent[b] = a;
		}
	}

	static int find(int k) {
		if (parent[k] != k) {
			parent[k] = find(parent[k]);
		}

		return parent[k];
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		// 사람의 수
		int N = Integer.parseInt(st.nextToken());
		// 행사의 수
		int M = Integer.parseInt(st.nextToken());

		// 이미 알고있는 사람 집합
		st = new StringTokenizer(br.readLine());
		int knowPersonCount = Integer.parseInt(st.nextToken());
		int[] knowPerson = new int[knowPersonCount];
		for (int i = 0; i < knowPersonCount; i++) {
			knowPerson[i] = Integer.parseInt(st.nextToken());
		}

		parent = new int[N + 1];
		for (int i = 0; i <= N; i++) {
			parent[i] = i;
		}

		// 행사 리스트
		int[][] eventsPerson = new int[M][];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int eventPersonCount = Integer.parseInt(st.nextToken());
			eventsPerson[i] = new int[eventPersonCount];
			for (int j = 0; j < eventPersonCount; j++) {
				eventsPerson[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 유니온파인드 진행
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < eventsPerson[i].length; j++) {
				for (int k = 0; k < eventsPerson[i].length; k++) {
					if (j == k) continue;
					union(eventsPerson[i][j], eventsPerson[i][k]);
				}
			}
		}

		for (int i = 1; i <= N; i++) {
			parent[i] = find(i);
		}


		// 이제 다시 행사별로 find 한 뒤에 교집합 하기
		int answer = 0;

		// 정답을 알고있는 무리
		Set<Integer> knowPersonSet = new HashSet<>();
		for (int i = 0; i < knowPerson.length; i++) {
			knowPersonSet.add(
					find(knowPerson[i])
			);
		}

		// 행사별 무리
		for (int i = 0; i < M; i++) {
			Set<Integer> perEventPersonSet = new HashSet<>();
			for (int j = 0; j < eventsPerson[i].length; j++) {
				perEventPersonSet.add(
						find(eventsPerson[i][j])
				);
			}

			perEventPersonSet.retainAll(knowPersonSet);
			if (perEventPersonSet.isEmpty()) {
				answer++;
			}
		}

		System.out.println(answer);

	}
}
