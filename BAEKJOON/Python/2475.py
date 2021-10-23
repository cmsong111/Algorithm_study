lis = list(map(int,input().split()))
for i in range(5):
    lis[i] = lis[i]**2
print(sum(lis)%10)

