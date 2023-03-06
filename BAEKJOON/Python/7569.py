from collections import deque
import sys
standard_input = """4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
"""


x, y, z = map(int, input().split())

box = [[] for _ in range(z)]


for i in range(z):
    for ii in range(y):
        box[i].append(list(map(int, input().split())))



dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()

for i in range(z):
    for ii in range(y):
        for iii in range(x):
            if box[i][ii][iii] == 1:
                queue.append((i, ii, iii))


result = 0

while queue:
    tz, ty, tx = queue.popleft()

    for i in range(6):
        nx = tx + dx[i]
        ny = ty + dy[i]
        nz = tz + dz[i]
        if 0 <= nx < x and 0 <= ny < y and 0 <= nz < z:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[tz][ty][tx] + 1
                queue.append((nz, ny, nx))

result = 0
flag = False
for i in range(z):
    for ii in range(y):
        for iii in range(x):
            if box[i][ii][iii] == 0:
                flag = True
                break
            if result < box[i][ii][iii]:
                result = box[i][ii][iii]
if flag:
    print(-1)
if not flag:
    print(result - 1)
