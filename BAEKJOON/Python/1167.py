standard_input ="""5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
"""

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def dfs(x, visited, graph, cost):
    visited[x] = True

    for i in graph[x]:
        if not visited[i[0]]:
            cost[i[0]] = cost[x] + i[1]
            dfs(i[0], visited, graph, cost)

V = int(input())

graph = [[] for _ in range(V + 1)]

# 그래프 생성
for i in range(V):
    temp = list(map(int, input().split()))

    for j in range(1, len(temp) - 1, 2):
        graph[temp[0]].append((temp[j], temp[j + 1]))


# 임의의 정점에서 가장 먼 정점을 구함
visited = [False] * (V + 1)
cost = [0] * (V + 1)
dfs(1, visited, graph, cost)

max_cost = 0
max_idx = 0

# 가장 먼 정점에서 가장 먼 정점을 구함
for i in range(1, V + 1):
    if max_cost < cost[i]:
        max_cost = cost[i]
        max_idx = i
    
# 가장 먼 정점에서 가장 먼 정점까지의 거리를 구함
visited = [False] * (V + 1)
cost = [0] * (V + 1)
dfs(max_idx, visited, graph, cost)

# 결과 출력
print(max(cost))

