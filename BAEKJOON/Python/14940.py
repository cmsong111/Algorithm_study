from collections import deque
import sys
standard_input = """2 5
1 1 1 1 2
0 0 0 0 0
"""


# input = sys.stdin.readline

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            result[i][j] = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# print result board
for i in range(N):
    for j in range(M):
        print(result[i][j], end=' ')
    print()


queue = deque()

# 시작점 찾기 (2)
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            result[i][j] = 0
            queue.append((i, j))
            break
print(queue)

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if result[nx][ny] == -1:
            result[nx][ny] = result[x][y] + 1
            queue.append((nx, ny))

# print result board
for i in range(N):
    for j in range(M):
        print(result[i][j], end=' ')
    print()
