a = int(input())
lis = []

for i in range(a):
    lis.append(int(input()))


print(max(lis))
print(lis.index(max(lis))+1)