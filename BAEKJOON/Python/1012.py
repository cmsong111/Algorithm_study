import sys
from collections import deque
testcase = int(sys.stdin.readline().rstrip())

for i in range(testcase):
    # 입력
    sizeX, sizeY, cabbage = map(int, sys.stdin.readline().split())
    # 상하좌우 0 한칸 더줌 (편의를 위해)
    sizeX += 2
    sizeY += 2

    arr = []
    check = []
    for i in range(sizeX):
        arr.append([0]*sizeY)
        check.append([0]*sizeY)

    for ii in range(cabbage):
        tempX, tempY = map(int, sys.stdin.readline().split())
        arr[tempX+1][tempY+1] = 1

    # for ii in arr:
    #     print(ii)

    que = deque()
    result = []

    for i in range(sizeX):
        for ii in range(sizeY):
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
                        # result[-1] += 1
                    # 하
                    if arr[now[0]+1][now[1]] == 1 and check[now[0]+1][now[1]] == 0:
                        que.append([now[0]+1, now[1]])
                        check[now[0]+1][now[1]] = 1
                        # result[-1] += 1
                    # 좌
                    if arr[now[0]][now[1]-1] == 1 and check[now[0]][now[1]-1] == 0:
                        que.append([now[0], now[1]-1])
                        check[now[0]][now[1]-1] = 1
                        # result[-1] += 1
                    # 우
                    if arr[now[0]][now[1]+1] == 1 and check[now[0]][now[1]+1] == 0:
                        que.append([now[0], now[1]+1])
                        check[now[0]][now[1]+1] = 1
                        # result[-1] += 1
    print(len(result))
