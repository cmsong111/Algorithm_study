class Solution {
	public static boolean isValid(long level, int[] diffs, int[] times, long limit) {
		long totalTime = times[0];
		for (int i = 1; i < times.length; i++) {
			int diff = diffs[i];
			int time = times[i];

			if (diff <= level) {
				// 현재 레벨 이하의 퍼즐은 시간만 더함
				totalTime += time;
			} else {
				// 현재 레벨보다 높은 퍼즐은 시간과 난이도 차이를 고려하여 계산
				totalTime += (time + times[i - 1]) * (diff - level) + time;
			}
		}
		return totalTime <= limit;
	}

	public static int solution(int[] diffs, int[] times, long limit) {
		int answer = 0;

		int left = 1;
		int right = 100000;
		while (left <= right) {
			int mid = (left + right) / 2; // 중간값 계산
//			System.out.println("left = " + left + ", right = " + right + ", mid = " + mid);

			if (isValid(mid, diffs, times, limit)) {
				// 현재 레벨(mid)에서 모든 퍼즐을 푸는 것이 가능하다면
				right = mid - 1; // 더 낮은 레벨을 시도
				answer = mid; // 가능한 레벨을 기록
			} else {
				// 현재 레벨(mid)에서 모든 퍼즐을 푸는 것이 불가능하다면
				left = mid + 1; // 더 높은 레벨을 시도
			}
		}


		return answer; // 해결 가능한 최대 퍼즐 개수 반환
	}
}
