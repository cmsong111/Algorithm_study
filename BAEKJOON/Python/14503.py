import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
result = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))


# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def cleanUp(x, y):
    """
    현재 위치가 아직 청소하지 않은 공간이라면 청소한다.
    """
    global graph, result
    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1


def checkAround(movable: bool = False):
    """
    현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인한다.\n
    movable이 True라면 주변이 청소되지 않은 0, 청소된 2인지 확인한다.\n
    movable이 False라면 청소되지 않은 칸이 있는지 확인한다.\n
    """
    global graph, r, c, d

    if movable:
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                return True
        return False
    else:
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if graph[nx][ny] == 0:
                return True
        return False


def goBack():
    """
    현재 방향에서 후진할 수 있는지 확인한다.\n
    후진할 수 있다면 True, 없다면 False를 반환한다.
    """
    global graph, r, c, d
    # 방향 전환
    d = (d+2) % 4

    nx = r + dx[d]
    ny = c + dy[d]

    # 벽이라면 종료
    if graph[nx][ny] == 1:
        d = (d+2) % 4
        return False

    # 후진
    r = nx
    c = ny
    d = (d+2) % 4
    return True


def turnLeft():
    """
    현재 방향에서 왼쪽으로 방향을 전환한다.
    바라보는 방향이 청소되지 않은 공간이라면 그 방향으로 전환한다.    
    """
    global graph, r, c, d
    d = (d+3) % 4

    nx = r + dx[d]
    ny = c + dy[d]

    if graph[nx][ny] == 0:
        r = nx
        c = ny
        return True


while True:
    # 1. 현재 위치를 청소한다.
    cleanUp(r, c)
    # 3. 청소할 공간이 있을때 왼쪽으로 회전하고 1번부터 진행한다.
    if checkAround(movable=False):
        turnLeft()
        continue

    # 2. 청소할 공간이 없을때 후진 혹은 종료한다.
    if checkAround(movable=True):
        if goBack():
            continue
        else:
            break

    else:
        break


print(result)
