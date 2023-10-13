standard_input ="""103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107"""


arr = []
for i in range(9):
    arr.append(list(map(int, input())))

def check(x, y, num):
    for i in range(9):
        if arr[x][i] == num:
            return False
        if arr[i][y] == num:
            return False
    for i in range(3):
        for j in range(3):
            if arr[(x//3)*3 + i][(y//3)*3 + j] == num:
                return False
    return True


def dfs(cnt):
    if cnt == 81:
        for i in arr:
            print(''.join(map(str, i)))
        exit()
    x = cnt // 9
    y = cnt % 9
    if arr[x][y] == 0:
        for i in range(1, 10):
            if check(x, y, i):
                arr[x][y] = i
                dfs(cnt + 1)
                arr[x][y] = 0
    else:
        dfs(cnt + 1)

dfs(0)