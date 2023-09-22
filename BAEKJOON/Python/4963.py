standard_input ="""1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0"""

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def dfs(x, y, visited, graph, w, h):
    visited[x][y] = True

    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny, visited, graph, w, h)


while(True):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []

    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    visited = [[False] * w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, visited, graph, w, h)
                count += 1
    
    print(count)

    