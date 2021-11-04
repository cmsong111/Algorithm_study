count = int(input())

for i in range(1,count+1):
    print(" "*(count-i),end="")
    print("*"*(i),end="")
    print("*"*(i-1),end="")
    print()

for i in range(count-1,0,-1):
    print(" "*(count-i),end="")
    print("*"*(i),end="")
    print("*"*(i-1),end="")
    print()
