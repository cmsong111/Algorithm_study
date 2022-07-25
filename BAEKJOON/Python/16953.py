from collections import deque
import sys

start, target = map(int, sys.stdin.readline().split())


que = deque()
que.append([start, 1])

result = temp = 0
check = 1
result = -1

while(que):
    now = que.popleft()
    # print(now)

    if now[0] == target:  # 타켓이면 정지
        result = now[1]
        break

    if now[0]*10+1 <= target:
        que.append([now[0]*10+1, now[1]+1])

    if now[0]*2 <= target:
        que.append([now[0]*2, now[1]+1])

#     print(que)

# print(que)
print(result)
