import copy
import sys

# 재귀 한도 설정
sys.setrecursionlimit(10**6)

standard_input ="""5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR"""  

def print_arr(arr):
    """arr 출력 함수"""
    for i in range(N):
        print(*arr[i])
    print()

def dfs(x, y, arr, visited):
    """dfs 함수"""
    visited[x][y] = True
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                dfs(nx, ny, arr, visited)



# 입력
N = int(input())

origin = [list(input()) for _ in range(N)]
blind = copy.deepcopy(origin)

visited = [[False] * N for _ in range(N)]
visited_blind = [[False] * N for _ in range(N)]

result = 0
result_blind = 0

direction = [(1,0), (-1,0), (0,1), (0,-1)]

# 적록색약 (R,G,B) -> (R,G)로 인식
for i in range(N):
    for j in range(N):
        if blind[i][j] == 'R':
            blind[i][j] = 'G'

# dfs
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, origin, visited)
            result += 1
        if not visited_blind[i][j]:
            dfs(i, j, blind, visited_blind)
            result_blind += 1


print(result, result_blind)
