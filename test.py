a = list(input().split("-"))
for i in range(len(a)):
    b = []
    b.append(a[i].split("+"))
    temp = 0
    for i1 in range(len(b)):
        for i2 in range(len(b[i1])):
            tmp = b[i1][i2]
            temp = temp + int(tmp)
    a[i] = int(temp)

sum = int(a[0])
for i in range(1,len(a),1):
    sum -=int(a[i])
print(sum)