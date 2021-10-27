import sys
stack = []
for i in range(int(sys.stdin.readline().strip())):
    a = sys.stdin.readline().strip()
    try:   
        a,b = a.split(' ')
    except:
        pass
#푸쉬
    if a == "push":
        stack.append(b)
#pop   
    elif a == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[0])
            del stack[0]
#size
    elif a == "size":
        print(len(stack))
#empty
    elif a == "empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
#front
    elif a == "front":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[0])
#back
    elif a == "back":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])