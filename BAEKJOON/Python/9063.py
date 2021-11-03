x=[]
y=[]
for i in range(int(input())):
    temp1,temp2 = map(int,input().split())
    x.append(temp1)
    y.append(temp2)
print((max(x)-min(x))*(max(y)-min(y)))
