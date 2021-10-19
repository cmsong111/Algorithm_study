a = int(input())
lis = []
for i in range(a):
    a,b =map(int,input().split())
    temp = [a,b]
    lis.append(temp)

lis.sort()

for i in range(len(lis)):
    for i1 in range(2):
        print(lis[i][i1],end=" ")
    print()