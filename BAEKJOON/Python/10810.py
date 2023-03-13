import sys

N,M = map(int,input().split())

arr = [0] * (N+1)

for i in range(M):
    a,b,c = map(int,input().split())
    
    for i in range(a,b+1):
        arr[i] = c

for i in range(1,N+1):
    print(arr[i],end=" ")