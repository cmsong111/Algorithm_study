result = []
for i in range(int(input())):
    temp = int(input())
    if temp == 0:
        if len(result) != 0:
            result.pop()
    else:
        result.append(temp)

print(sum(result))