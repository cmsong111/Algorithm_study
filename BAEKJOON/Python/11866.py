a,b = map(int,input().split())
member = list(range(1,a+1))
result = []


while(len(member)>=b):
    result.append(member[b-1])
    temp = member[0:b-1]
    del(member[b-1])
    del(member[0:b-1])
    for i in range(len(temp)):
        member.append(temp[i])
while(len(member) > 1):
    count = (b%len(member))
    result.append(member[count-1])
    tmp = member[:count]
    if len(tmp)== 0:
        del(member[len(member)-1])
    else:
        del(member[:count])
        for i in range(len(tmp)-1):
            member.append(tmp[i])


if len(member) == 1:
    result.append(member[0])


print("<",end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(result[a-1],">",sep="")
