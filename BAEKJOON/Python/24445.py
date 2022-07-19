
import sys
from collections import deque

vertax, edge, start = map(int, sys.stdin.readline().split())

grahp = []


for i in range(vertax+1):
    grahp.append([])

for i in range(edge):
    target1, target2 = map(int, sys.stdin.readline().split())
    grahp[target1].append(target2)
    grahp[target2].append(target1)

for i in grahp:
    i.sort(reverse=True)


# 너비
check = [0]*(vertax+1)
que = deque()
que.append(start)
distance = 0
while(que):
    now = que.popleft()
    if check[now] == 0:
        que.extend(grahp[now])
        distance += 1
        check[now] = distance


for i in range(1, vertax+1, 1):
    print(check[i])
