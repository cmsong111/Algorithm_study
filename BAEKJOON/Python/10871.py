a,b = map(int,input().split())
lis = list(map(int,input().split()))
for i in range(a):
    if lis[i] < b:
        print(lis[i],sep="",end=" ")
print()