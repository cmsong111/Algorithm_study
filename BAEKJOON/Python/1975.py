standard_input = """4 6
a t c i s w
"""

from itertools import combinations

a,b = map(int, input().split())

c = input().split()
c.sort()

d = list(combinations(c, a))


def check(x):
    arr = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in x:
        if i in arr:
            cnt += 1
    if cnt >= 1 and cnt <= a-2:
        return True
    else:
        return False

for i in d:
    if check(i):
        print(''.join(i))

