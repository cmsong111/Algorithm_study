import sys
from itertools import combinations

input = sys.stdin.readline

arr =[]

for i in range(9):
    arr.append(int(input()))

result = combinations(arr, 7)


for i in result:
    if sum(i) == 100:
        for i in sorted(i):
            print(i)
        break

