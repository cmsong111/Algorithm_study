lis = []

for i in range(10):
    a= int(input())
    if (a % 42) not in lis:
        lis.append(a%42)

print(len(lis))

        