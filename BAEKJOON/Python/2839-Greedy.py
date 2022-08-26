# import sys

standard_input = """3"""

# 백준 제출시 주석 해제
# input = sys.stdin.readline

target = int(input())

result = 0

while (target >= 0):
    if target % 5 == 0:
        result += (target // 5)
        print(result)
        break

    target -= 3
    result += 1
else:
    print(-1)
