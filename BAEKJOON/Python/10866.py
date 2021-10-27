from collections import deque
import sys

deq = deque()
for i in range(int(sys.stdin.readline().strip())):
    a = sys.stdin.readline().strip()
    try:   
        a,b = a.split(' ')
    except:
        pass

    #push_back
    if a == "push_back":
        deq.append(b)
    #push_front
    elif a == "push_front":
        deq.appendleft(b)
    #pop_front
    elif a == "pop_front":
        if len(deq)==0:
            print("-1")
        else:
            print(deq.popleft())
    #pop_back
    elif a == "pop_back":
        if len(deq)==0:
            print("-1")
        else:
            print(deq.pop())
    #size
    elif a == "size":
        print(len(deq))
    #empty
    elif a == "empty":
        if len(deq)==0:
            print("1")
        else:
            print("0")
    #front
    elif a == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    #back
    elif a == "back":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[-1])