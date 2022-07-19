import sys
from itertools import *

while(1):
    a = list(map(int,sys.stdin.readline().split()))
    if a == [0]:
        break
    a.remove(a[0])
    a.sort()
    result = list(combinations(a,6))
    for i in result:
        for ii in i:
            print(ii,end=" ")
        print()
    print()