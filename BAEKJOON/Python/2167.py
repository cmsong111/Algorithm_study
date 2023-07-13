standard_input = """2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
"""

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(sum([sum(matrix[i-1][j-1:y]) for i in range(i, x+1)]))
