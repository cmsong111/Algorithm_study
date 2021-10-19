import sys

count = int(input())
lis = []
for i in range(count):
    a,b,c,d = map(int,sys.stdin.readline().split())
    lis.append([b*c*d, b+c+d, a])

lis.sort()

for i in range(3):
    print(lis[i][2],end=" ")
