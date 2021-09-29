a,b = map(int,input().split())
lis = list(map(int,input().split()))
num = []
for i1 in range (a):
    for i2 in range (a):
        for i3 in range (a):
            if (lis[i1]+lis[i2]+lis[i3]) <= b:
                if i1 != i2:
                    if i2 != i3:
                        if i1 != i3:
                            num.append(lis[i1]+lis[i2]+lis[i3])
print(max(num))
