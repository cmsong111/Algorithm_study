x = input()

for i in range(len(x)):
    temp = str(ord(x[i]))
    count = 0
    for i2 in range(len(temp)):
        count = count + int(temp[i2])
    print(x[i]*count)
