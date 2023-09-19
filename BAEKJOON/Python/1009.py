standard_input = """1
10 1"""


N = int(input())


num_index = [
    [0],
    [1],
    [2, 4, 8, 6],
    [3, 9, 7, 1],
    [4, 6],
    [5],
    [6],
    [7, 9, 3, 1],
    [8, 4, 2, 6],
    [9, 1]
]

for i in range(N):
    a, b = map(int, input().split())
    a = a % 10
    b = b % len(num_index[a])
    print(num_index[a][b-1])
