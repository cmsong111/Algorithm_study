import numpy as np


h,w = map(int,input().split())
n = int(input())


lis = np.zeros((h,w),int)

for i in range(n):
    I,d,x,y = map(int,input().split())
    if d==0:
        for i in range(I):
            lis[x-1][y-1+i] = 1
    if d==1:
        for i in range(I):
            lis[x-1+i][y-1] = 1
    



#출력부
for i in range(h):
    for j in range(w):
        print(lis[i][j],end=" ")
    print()
