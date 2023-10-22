standard_input = """5 4
1 2
3 4
1 4
2 2"""

N, M = map(int, input().split())

arr = list(range(1, N+1))

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1:b] = arr[a-1:b][::-1]

print(*arr)
