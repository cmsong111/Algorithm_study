#import sys

standard_input = """2
6
22
"""

# 백준 제출시 주석 해제
#input = sys.stdin.readline

cache = {0: [1, 0], 1: [0, 1], 2: [1, 1]}


def fibonacci(n: int):
    global cache
    if n in cache:
        return cache[n]
    else:
        target1 = fibonacci(n-1)
        target2 = fibonacci(n-2)
        cache[n] = [target1[0]+target2[0], target1[1]+target2[1]]
        return cache[n]


testcast = int(input())

for i in range(testcast):
    target = int(input())
    result = fibonacci(target)
    print(result[0], result[1])

# print(cache)
