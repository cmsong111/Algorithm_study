import sys
standard_input = """1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""

# input = sys.stdin.readline

# 빈 배열을 만들고, 직사각형이 그려지는 부분을 1로 채워준다.
arr = [[0] * 101 for _ in range(101)]

# 직사각형이 그려지는 부분을 1로 채워준다.
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

ans = 0

# 1로 채워진 부분을 세준다.
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            ans += 1

print(ans)
