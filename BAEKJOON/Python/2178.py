from collections import deque
import sys


sizeX, sizeY = map(int, sys.stdin.readline().split())

arr = []
check = []
bfs = deque()
bfs.append([1, 1])

# arr 입력
sizeY += 2
arr.append([0]*sizeY)
for i in range(sizeX):
    temp = [0]
    temp.extend(list(map(int, sys.stdin.readline().strip())))
    temp.append(0)
    arr.append(temp)
arr.append([0]*sizeY)
sizeX += 2

# check arr 생성
for i in range(sizeX):
    check.append([0]*sizeY)

check[1][1] = 1

# print("arr")
# for i in range(sizeX):
#     for ii in range(sizeY):
#         print(arr[i][ii], end="\t")
#     print()


# print("check")
# for i in range(sizeX):
#     for ii in range(sizeY):
#         print(check[i][ii], end="\t")
#     print()

# print(bfs)

while(arr[sizeX-2][sizeY-2] == 1):
    now = bfs.popleft()
    # print(now)

    # 위쪽
    if(arr[now[0]-1][now[1]] != 0 and check[now[0]-1][now[1]] == 0):
        arr[now[0]-1][now[1]] = arr[now[0]][now[1]]+1
        check[now[0]-1][now[1]] = 1
        bfs.append([now[0]-1, now[1]])

    # 아래
    if(arr[now[0]+1][now[1]] != 0 and check[now[0]+1][now[1]] == 0):
        arr[now[0]+1][now[1]] = arr[now[0]][now[1]]+1
        check[now[0]+1][now[1]] = 1
        bfs.append([now[0]+1, now[1]])

    # 왼쪽
    if(arr[now[0]][now[1]-1] != 0 and check[now[0]][now[1]-1] == 0):
        arr[now[0]][now[1]-1] = arr[now[0]][now[1]]+1
        check[now[0]][now[1]-1] = 1
        bfs.append([now[0], now[1]-1])

    # 오른쪽
    if(arr[now[0]][now[1]+1] != 0 and check[now[0]][now[1]+1] == 0):
        arr[now[0]][now[1]+1] = arr[now[0]][now[1]]+1
        check[now[0]][now[1]+1] = 1
        bfs.append([now[0], now[1]+1])

    # print("arr")
    # for i in range(sizeX):
    #     for ii in range(sizeY):
    #         print(arr[i][ii], end="\t")
    #     print()

    # print("check")
    # for i in range(sizeX):
    #     for ii in range(sizeY):
    #         print(check[i][ii], end="\t")
    #     print()

    # print(bfs)
    # print()
    # print()

print(arr[sizeX-2][sizeY-2])
