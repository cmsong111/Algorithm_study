count = int(input())

for i in range(count):
    a,b = input().split()
    a = int(a)
    x = len(b)
    for i in range(x):
        print(b[i]*a,sep="",end="")
    print()


