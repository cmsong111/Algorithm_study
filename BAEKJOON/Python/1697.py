import sys
from collections import deque
MAX = 10 ** 5


def bfs(n, k):
    Q = deque([n])
    dist = [0] * (MAX + 1)
    
    while Q:
        cur = Q.popleft()
        if cur == k:
            print(dist[cur])
            break
        
        for i in (cur - 1, cur + 1, cur * 2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[cur] + 1
                Q.append(i)


N,K = map(int,sys.stdin.readline().split())
bfs(N, K)