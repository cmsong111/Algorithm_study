import numpy as np



#배열 생성
lis = np.empty((0,10),int)

#배열 입력
for i in range(10):
    a=list(map(int,input().split()))
    lis = np.append(lis, np.array([a]), axis=0)

x,y= map(int,2,2)




#결과물 출력
for i in range(10):
    for j in range(10):
        print(lis[i][j],end=" ")
    print()
