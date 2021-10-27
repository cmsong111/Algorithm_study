from collections import deque

import sys
deq = deque()
for i in range(int(sys.stdin.readline().strip())):
    a = sys.stdin.readline().strip()
  
    try:   
        a,b = a.split(' ')
    except:
        pass

    print(a)

    if a == "pop_front":
        if len(deq)==0:
            print("-1")
        else:
            deq.popleft()
    #pop_back
    elif a == "pop_back":
        if len(deq)==0:
            print("-1")
        else:
            deq.pop()
    #push_back
    elif a == "push_back":
        deq.append(b)
    #push_front
    elif a == "push_front":
        deq.appendleft(b)

        