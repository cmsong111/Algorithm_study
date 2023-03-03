standard_input = """4 2
9 7 9 1
"""

import sys
from itertools import *

#input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ans = permutations(arr, k)

ans = set(ans)

ans = list(ans)

ans.sort()

for i in ans:
    for ii in i:
        print(ii, end=' ')
    print()