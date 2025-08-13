import java.util.*;

class Solution {
	public static int solution(int[][] points, int[][] routes) {
		Robot[] robots = new Robot[routes.length];

		for (int i = 0; i < routes.length; i++) {
			int startX = points[routes[i][0] - 1][0];
			int startY = points[routes[i][0] - 1][1];
			robots[i] = new Robot(
					startX, startY
			);

			for (int route : routes[i]) {
				int targetX = points[route - 1][0];
				int targetY = points[route - 1][1];
				robots[i].route.add(new Position(targetX, targetY));
			}

		}
		int answer = dangerousRobots(robots);
		while (Arrays.stream(robots).anyMatch(robot -> !robot.route.isEmpty())) {
			for (Robot robot : robots) {
				robot.move();
			}
			answer += dangerousRobots(robots);
		}

		return answer;
	}

	private static int dangerousRobots(Robot[] robots) {
		Map<Position, Integer> map = new HashMap<>();
		for (Robot robot : robots) {
			if (robot.route.isEmpty()) continue;

			if (map.containsKey(robot.currentPosition)) {
				map.put(robot.currentPosition, map.get(robot.currentPosition) + 1);
			} else {
				map.put(robot.currentPosition, 1);
			}
		}

//		System.out.println("map = " + map);

		return map.values().stream()
				.filter(integer -> integer > 1)
				.mapToInt(i -> 1)
				.sum();
	}

	static class Position {
		int x;
		int y;

		public Position(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public boolean equals(Object o) {
			if (this == o) return true;
			if (!(o instanceof Position)) return false;
			Position position = (Position) o;
			return x == position.x && y == position.y;
		}

		@Override
		public int hashCode() {
			return 31 * (x + ":" + y).hashCode();
		}

		@Override
		public String toString() {
			return "Position{" +
					"x=" + x +
					", y=" + y +
					'}';
		}
	}

	static class Robot {
		Position currentPosition;
		Deque<Position> route;

		public Robot(int startX, int startY) {
			this.currentPosition = new Position(startX, startY);
			this.route = new java.util.ArrayDeque<>();
		}

		void move() {
				// 도착 위치에 도달했으면
			if (currentPosition.equals(route.peek())) {
				route.poll();
			}
            // 도착 위치에 도달했는지 확인
			if (route.isEmpty()) {
				return;
			}
			if (currentPosition.x != route.peek().x) {
				if (currentPosition.x < route.peek().x) {
					currentPosition.x++;
				} else {
					currentPosition.x--;
				}
			} else if (currentPosition.y != route.peek().y) {
				if (currentPosition.y < route.peek().y) {
					currentPosition.y++;
				} else {
					currentPosition.y--;
				}
			}

		}
	}
}
