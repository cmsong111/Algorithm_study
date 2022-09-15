from collections import deque
import sys

input = sys.stdin.readline

que = deque()
count = int(input().rstrip())

for i in range(count):
    temp = input().rstrip()
    if "push"  in temp:
        a, b = temp.split()
        b = int(b)
        que.append(b)
    elif temp == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif temp == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
    elif temp == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif temp == "size":
        print(len(que))
    elif temp == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
