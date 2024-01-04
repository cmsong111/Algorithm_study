import sys
import copy
from collections import deque
standard_input = """5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""

# input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

N = int(input())

answer = 0

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


# print("graph:")
# for i in graph:
#     print(*i)

max_height = max(map(max, graph))

# print(max_height)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > height and not visited[nx][ny]:
                dfs(nx, ny, visited)


for height in range(max_height):
    temp_graph = copy.deepcopy(graph)

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] <= height:
                temp_graph[i][j] = 0
            else:
                temp_graph[i][j] = 1

    # print("temp_graph:")
    # for i in temp_graph:
    #     print(*i)

    count = 0

    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited)
                count += 1

    if count > answer:
        answer = count

    # print("count:", count)
    # print()

print(answer)
