#import sys

standard_input = """5"""

# 백준 제출시 주석 해제
#input = sys.stdin.readline

target = int(input())
cache = [-1]*(target+1)

cache[3] = 1

if target >= 5:
    cache[5] = 1

for i in range(6, target+1, 1):
    if cache[i-3] > 0 or cache[i-5] > 0:
        if cache[i-3] > 0 and cache[i-5] > 0:
            cache[i] = min(cache[i-3], cache[i-5])+1
        else:
            cache[i] = max(cache[i-3], cache[i-5])+1

# for i in range(target):
#     print(i, cache[i])

print(cache[target])
