import sys
stack = []
for i in range(int(sys.stdin.readline().strip())):
    a = sys.stdin.readline().strip()
    try:   
        a,b = a.split(' ')
    except:
        pass

    if a == "push":
        stack.append(b)
        
    elif a == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif a == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])