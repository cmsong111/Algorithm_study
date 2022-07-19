import sys
from collections import deque

# 입력부
size = int(sys.stdin.readline().rstrip())
arr = []
size += 2
arr.append([0]*size)
for i in range(size-2):
    temparr = sys.stdin.readline().rstrip()
    temp = [0]
    for i in temparr:
        temp.append(int(i))
    temp.append(0)
    arr.append(temp)

arr.append([0]*size)

# 처리부

# 체크
check = []
result = []
que = deque()

for i in range(size):
    check.append([0]*size)

# for i in arr:
#     print(i)
# print()
# for i in check:
#     print(i)


for i in range(size):
    for ii in range(size):
        # print("checking now", i, ii, "arr:",
        #       arr[i][ii], "check:", check[i][ii])
        if arr[i][ii] == 1 and check[i][ii] == 0:
            que.append([i, ii])  # 큐 추가
            check[i][ii] = 1  # 왔다감
            result.append(1)  # 결과

            while(que):
                now = que.popleft()
                # 상
                if arr[now[0]-1][now[1]] == 1 and check[now[0]-1][now[1]] == 0:
                    que.append([now[0]-1, now[1]])
                    check[now[0]-1][now[1]] = 1
                    result[-1] += 1
                # 하
                if arr[now[0]+1][now[1]] == 1 and check[now[0]+1][now[1]] == 0:
                    que.append([now[0]+1, now[1]])
                    check[now[0]+1][now[1]] = 1
                    result[-1] += 1
                # 좌
                if arr[now[0]][now[1]-1] == 1 and check[now[0]][now[1]-1] == 0:
                    que.append([now[0], now[1]-1])
                    check[now[0]][now[1]-1] = 1
                    result[-1] += 1
                # 우
                if arr[now[0]][now[1]+1] == 1 and check[now[0]][now[1]+1] == 0:
                    que.append([now[0], now[1]+1])
                    check[now[0]][now[1]+1] = 1
                    result[-1] += 1
            #     print("check")
            #     for iii in check:
            #         print(iii)
            # print(que)
            # print("result", end=":")
            # print(result)


print(len(result))
result.sort()
for i in result:
    print(i)
