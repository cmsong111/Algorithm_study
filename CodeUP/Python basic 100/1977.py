import math

a = int(input())
b = int(input())

lis = []

for i in range(a,b+1,1):
    if math.sqrt(i)%1 == 0:
        lis.append(i)

if len(lis)==0:
    print("-1")
else:
    print(sum(lis))
    print(min(lis))