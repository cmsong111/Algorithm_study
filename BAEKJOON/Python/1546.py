a= int(input())
lis = list(map(int,input().split()))

maximun = max(lis)

for i in range(a):
    lis[i] = lis[i] / maximun * 100

print(sum(lis)/a)