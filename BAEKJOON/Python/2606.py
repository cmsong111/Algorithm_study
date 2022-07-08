import sys
from collections import deque
input = sys.stdin.readline

# 입력
vertaxcount = int(input().rstrip())
edgecount = int(input().rstrip())

arr = []
bfs = deque()

check = [0]*vertaxcount
check[0] = 1

for i in range(vertaxcount):
    temp = []
    arr.append(temp)

# 입력
for i in range(edgecount):
    a, b = map(int, input().split())
    arr[a-1].append(b)
    arr[b-1].append(a)


# 출력
# print('arr:')
# for i in range(vertaxcount):
#     print(i+1, end=" ")
#     print(arr[i])

bfs.extend(arr[0])

while(bfs):
    # print(bfs)
    # print(check)
    now = bfs.popleft()

    if check[now-1] == 0:
        check[now-1] = 1
        bfs.extend(arr[now-1])

# print(bfs)
# print(check)
print(sum(check)-1)
