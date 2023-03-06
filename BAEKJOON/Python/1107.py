import sys
from itertools import product
standard_input = """2229
6
4 5 6 7 8 9
"""

# input = sys.stdin.readline

channel = 100
target = int(input())
broken_len = int(input())

target_len = len(str(target))


broken = []
if broken_len != 0:
    broken = list(map(int, input().split()))

available = [i for i in range(10)]

for i in broken:
    available.remove(i)

arr = product(available, repeat=target_len)
arr1 = product(available, repeat=target_len+1)
arr2 = []
if target_len > 1:
    arr2 = product(available, repeat=target_len-1)


result = abs(target - channel)

for i in arr:
    value = 0
    for ii in range(target_len):
        value += i[ii] * (10 ** (target_len - ii - 1))
    temp = abs(target - value) + len(str(value))
    #print(value, temp)
    if temp < result:
        result = temp

for i in arr1:
    value = 0
    for ii in range(target_len+1):
        value += i[ii] * (10 ** (target_len - ii))
    temp = abs(target - value) + len(str(value))
    #print(value, temp)
    if temp < result:
        result = temp

for i in arr2:
    value = 0
    for ii in range(target_len-1):
        value += i[ii] * (10 ** (target_len - ii - 2))
    temp = abs(target - value) + len(str(value))
    #print(value, temp)
    if temp < result:
        result = temp


print(result)
