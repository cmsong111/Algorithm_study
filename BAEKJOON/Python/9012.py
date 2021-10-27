import sys
for i in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().rstrip())
    
    sum = 0
    for i in a:
        if i == "(":
            sum +=1
        elif i == ")":
            sum -=1
        if sum < 0:
            print("NO")
            break
    
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")