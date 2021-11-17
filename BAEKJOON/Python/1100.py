import sys
result = 0
a =[]
for i in range(8):
    temp = sys.stdin.readline().strip()
    tmp = []
    for i1 in range(8):
        tmp.append(temp[i1])
    a.append(tmp)


for i in range(8):
    for i1 in range(8):
        if (i+i1)%2 == 0:
            if a[i][i1] =="F":
                result+=1

print(result)
