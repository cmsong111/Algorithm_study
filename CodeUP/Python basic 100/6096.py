import numpy as np
#뒤집기 명령어
def turn(a):
    if a == 0:
        return 1
    elif a == 1:
        return 0


#배열 생성
lis = np.empty((0,19),int)

#배열 입력
for i in range(19):
    a=list(map(int,input().split()))
    lis = np.append(lis, np.array([a]), axis=0)

#명령어 입력
n = int(input())

for i1 in range(n):
    x,y= map(int,input().split())

    for i2 in range(19):
        lis[i2][y-1]=turn(lis[i2][y-1])
        lis[x-1][i2] = turn(lis[x-1][i2])

#결과물 출력
for i in range(19):
    for j in range(19):
        print(lis[i][j],end=" ")
    print()
