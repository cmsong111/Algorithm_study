import sys
from collections import deque

sizeX, sizeY = map(int, sys.stdin.readline().split())
sizeX += 2
sizeY += 2

arr = []
arr.append([-1]*sizeX)
for i in range(sizeY-2):
    temp = [-1]
    temp.extend(list(map(int, sys.stdin.readline().split())))
    temp.append(-1)
    arr.append(temp)
arr.append([-1]*sizeX)

# print("arr")
# for i in arr:
#     for ii in i:
#         print(ii, end='\t')
#     print()

check = []
for i in arr:
    temp = []
    for ii in i:
        if ii == -1:
            temp.append(1)
        else:
            temp.append(0)
    check.append(temp)

# print("check")
# for i in check:
#     for ii in i:
#         print(ii, end='\t')
#     print()


que = deque()
result = []
arrtemp = []


for i in range(sizeY):
    for ii in range(sizeX):
        if arr[i][ii] == 1:
            arrtemp.append([i, ii])
            # que.append([i, ii])  # 큐 추가
            check[i][ii] = 1
            arr[i][ii] = 1   # 왔다감
            result.append(1)  # 결과
que.append(list(arrtemp))

count = -1
while(que[0]!=[]):
    temp = que.popleft()
    count += 1
    arrtemp = []
    for now in temp:
        # 상
        if arr[now[0]-1][now[1]] == 0 and check[now[0]-1][now[1]] == 0:
            arrtemp.append([now[0]-1, now[1]])
            check[now[0]-1][now[1]] = 1
            arr[now[0]-1][now[1]] = count
            # result[-1] += 1
        # 하
        if arr[now[0]+1][now[1]] == 0 and check[now[0]+1][now[1]] == 0:
            arrtemp.append([now[0]+1, now[1]])
            check[now[0]+1][now[1]] = 1
            arr[now[0]+1][now[1]] = count
            # result[-1] += 1
        # 좌
        if arr[now[0]][now[1]-1] == 0 and check[now[0]][now[1]-1] == 0:
            arrtemp.append([now[0], now[1]-1])
            check[now[0]][now[1]-1] = 1
            arr[now[0]][now[1]-1] = count
            # result[-1] += 1
        # 우
        if arr[now[0]][now[1]+1] == 0 and check[now[0]][now[1]+1] == 0:
            arrtemp.append([now[0], now[1]+1])
            check[now[0]][now[1]+1] = 1
            arr[now[0]][now[1]+1] = count
            # result[-1] += 1
    que.append(arrtemp)


# print("arr")
# for i in arr:
#     for ii in i:
#         print(ii, end='\t')
#     print()

# print("check")
# for i in check:
#     for ii in i:
#         print(ii, end='\t')
#     print()

printed = 1
for i in check:
    for ii in i:
        if ii == 0:
            if printed:
                print("-1")
                printed=0

if printed:
    print(count)



