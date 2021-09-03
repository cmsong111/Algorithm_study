import numpy as np
a=np.zeros((19,19))

n= int(input())

for i in range(n):
    x,y= map(int, input().split())
    a[x-1][y-1]=1


for i in range(19):
    for j in range(19):
        print(int(a[i][j]),end=" ")
    print()
