import sys
from collections import Counter


x = int(sys.stdin.readline())
xl = list(sys.stdin.readline().split())
y = int(sys.stdin.readline())
yl = list(sys.stdin.readline().split())

xl.sort()
count = Counter(xl)

for i in range(len(yl)):
    if yl[i] in count:
        print(count[yl[i]],end=" ")
    else:
        print("0",end=" ")