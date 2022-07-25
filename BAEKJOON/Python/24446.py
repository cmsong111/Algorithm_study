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
    i.sort()


# 너비
check = [-1]*(vertax+1)
que = deque()
que.append([start])

distance = 0
while(que[0] != []):
    #print(que)
    now = que.popleft()
    #print(now)
    temp = []
    for i in now:
        if check[i] == -1:
            check[i] = distance
            temp.extend(grahp[i])
    que.append(temp)
    # print(temp)
    # print(que)
    distance +=1

    # if now == -100:
    #     distance +=1
    # elif check[now] == -1:
    #     que.extend(grahp[now])
        
    #     check[now] = distance 

# check[start] = 0

del(check[0])

for i in check:
    print(i)