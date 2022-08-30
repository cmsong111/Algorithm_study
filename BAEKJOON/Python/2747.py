#import sys

standard_input = """10"""

# 백준 제출시 주석 해제
#input = sys.stdin.readline

cache = {0: 0, 1: 1, 2: 1}


def fibonacci(n: int):
    global cache
    if n in cache:
        return cache[n]
    else:
        target1 = fibonacci(n-1)
        target2 = fibonacci(n-2)
        cache[n] = target1+target2
        return cache[n]


target = int(input())
result = fibonacci(target)
print(result)


