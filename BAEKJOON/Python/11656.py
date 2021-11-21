temp = input()

result = []
for i in range(len(temp)):
    result.append(temp[i:])

result.sort()

for i in result:
    print(i)