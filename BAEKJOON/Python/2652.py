
lis = []

for i in range(9):
    lis.append(int(input()))


print(max(lis))
print(lis.index(max(lis))+1)