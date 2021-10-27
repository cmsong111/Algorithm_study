from collections import deque
import sys

number = int(sys.stdin.readline())

deq = deque()

for i in range(1,number+1):
    deq.append(i)

while(len(deq)!=1):
    deq.popleft()
    temp = deq.popleft()
    deq.append(temp)

print(deq[0])