a,b = map(int,input().split())
a = list(range(1,a+1))
result = []

while(len(a)>=b):
    temp = a.pop(b-1)
    result.append(temp)
    tmp = a[0:b-1]
    del a[0:b-1]
    for i in tmp:
        a.append(i)


while(len(a) != 0):
    count = (b-1) % len(a)

    result.append(a.pop(count))
    
    tmp = a[0:count]
    del a[0:count]
    for i in tmp:
        a.append(i)
    

print("<",end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(result[-1],">",sep="")
