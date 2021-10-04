num = int(input())
for i in range(num):
    no_star = num-i-1
    yes_star = i+1
    for i1 in range(no_star):
        print(" ",sep="",end="")
    for i2 in range(yes_star):
        print("*",sep="",end="")
    print()