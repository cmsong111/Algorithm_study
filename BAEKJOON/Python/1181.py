lis = []
for i in range(int(input())):
    lis.append(input())

a = set(lis)
lis = list(a)
lis.sort()
lis.sort(key = len)

for i in range(len(lis)):
    print(lis[i])
