x,y,w,h = map(int,input().split())

lis = []
lis.append(x)
lis.append(y)
lis.append(w-x)
lis.append(h-y)

print(min(lis))
