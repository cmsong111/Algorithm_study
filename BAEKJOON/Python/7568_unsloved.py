import sys
count = int(input())
lis = []
for i in range(count):
    x,y =map(int,input().split())
    lis.append([x,y,chr(i+65)])
    
print(lis)
ans = list(lis)
lis.sort()
lis.reverse()
print(lis)
x = 1
result = [1]
for i in range(count-1):
    if lis[i][0] > lis[i+1][0] and lis[i][1] > lis[i+1][1]:
        result.append(result[i]+x)
    else:
        result.append(result[i])
        x +=1


print("result = ",result)

temp = []
for i in range(count):
    temp.append([lis[i][2],result[i]])

print(temp)
temp.sort()
print(temp)

for i in range(count):
    print(temp[i][1],end=" ")