#import sys

standard_input = """2
6
12"""

# 백준 제출시 주석 해제
#input = sys.stdin.readline

cache = {0: 1, 1: 1, 2: 1}


def triangle(n: int):
    global cache
    if n in cache:
        return cache[n]
    else:
        target1 = triangle(n-2)
        target2 = triangle(n-3)
        cache[n] = target1+target2
        return cache[n]


testcase = int(input())
for i in range(testcase):
    target = int(input())
    result = triangle(target-1)
    print(result)
