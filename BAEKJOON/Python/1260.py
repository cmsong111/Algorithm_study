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

# for i in grahp:
#     print(i)


# 깊이
check = [0]*(vertax+1)
check[start] = 1
stack = [start]

print(start, end=" ")
while stack:
    flag = 0
    now = stack[-1]
    temp = grahp[now]
    if temp:
        for i in temp:
            if check[i] == 0:
                stack.append(i)
                check[i] = 1
                print(i, end=" ")
                break
            else:
                flag += 1
            if flag == len(temp):
                stack.pop()
    else:
        stack.pop()
print()


# 너비
check = [0]*(vertax+1)
que = deque()
que.append(start)

while(que):
    now = que.popleft()
    if check[now] == 0:
        que.extend(grahp[now])
        check[now] = 1
        print(now, end=" ")
