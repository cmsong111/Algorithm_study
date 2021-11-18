import sys
import heapq

a = []

for i in range(int(sys.stdin.readline().strip())):
    temp = int(sys.stdin.readline().strip())
    if temp == 0:
        if len(a) == 0:
            print("0")
        else:
            result = heapq.heappop(a)
            print(-result)
    else:
        heapq.heappush(a, -temp)