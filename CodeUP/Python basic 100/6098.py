import numpy as np

#배열 생성
lis = np.empty((0,10),int)

#배열 입력
for i in range(10):
    a=list(map(int,input().split()))
    lis = np.append(lis, np.array([a]), axis=0)

#시작점
x,y= map(int,(1,1))
lis[x][y]=9
while(1):
    if lis[x][y+1]==0: #오른쪽으로 이동
        y+=1
        lis[x][y]=9
        
    elif lis[x][y+1]==2: #오른쪽이 먹이라면
        lis[x][y]=9
        lis[x][y+1] =9
        break
        
    elif lis[x+1][y]==0: #아래쪽으로 이동
        x+=1
        lis[x][y]=9
        
    elif lis[x+1][y]==2:# 아래쪽이 먹이라면
        lis[x][y]=9
        lis[x+1][y]=9
        break
        
    else:
        break



#결과물 출력
for i in range(10):
    for j in range(10):
        print(lis[i][j],end=" ")
    print()
