standard_input = """5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""

import sys

def binary_serch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))

array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_serch(array, i, 0, n - 1)
    if result != None:
        print('1', end=' ')
    else:
        print('0', end=' ')