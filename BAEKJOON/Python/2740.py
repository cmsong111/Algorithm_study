import sys
standard_input = """3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3
"""

# input = sys.stdin.readline

n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())

b = []

for i in range(m):
    b.append(list(map(int, input().split())))


def matrix_mul(a, b):
    result = [[0 for _ in range(k)] for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for l in range(m):
                result[i][j] += a[i][l] * b[l][j]

    return result


result = matrix_mul(a, b)

for i in range(n):
    for j in range(k):
        print(result[i][j], end=' ')
    print()
