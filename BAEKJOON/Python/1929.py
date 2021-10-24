import math

n,m = map(int,input().split())
count = int(math.sqrt(m))

if n == 1:
    n += 1

lis = [True]*(m+1)

for i in range(2,count+1):
    if lis[i] == True:
        for j in range(i+i, m+1 , i):
            lis[j] = False

for i in range(n, m+1):
    if lis[i] == True:
        print(i)
