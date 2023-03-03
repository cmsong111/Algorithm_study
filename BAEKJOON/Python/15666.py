standard_input = """4 4
1 1 2 2
"""

import sys
from itertools import *

#input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ans = combinations_with_replacement(arr, k)

ans = set(ans)

ans = list(ans)

ans.sort()

for i in ans:
    for ii in i:
        print(ii, end=' ')
    print()