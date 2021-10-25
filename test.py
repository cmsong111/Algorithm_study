import sys
count = int(input())
lis = []
for i in range(count):
    x,y =map(int,input().split())
    lis.append([x,y,chr(i+65)])
    

ans = list(lis)
lis.sort()
lis.reverse()

x = 1
result = [1]
for i in range(count-1):
    if lis[i][0] > lis[i+1][0] and lis[i][1] > lis[i+1][1]:
        result.append(result[i]+x)
    else:
        result.append(result[i])
        x +=1

temp = []
for i in range(count):
    temp.append([lis[i][2],result[i]])


temp.sort()
print(temp)

for i in range(count-1):
    print(temp[i][1],end=" ")
print(temp[count-1][1])