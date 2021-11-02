temp = input()
count = len(temp)

lis = []
for i in range(count):
    lis.append(int(temp[i]))

lis.sort()
lis.reverse()

for i in lis:
    print(i,end="")