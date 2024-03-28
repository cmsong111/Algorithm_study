standard_input ="""5 4
1 2
3 4
1 4
2 2"""

n,m = map(int, input().split())

arr = list(range(1,n+1))

for _ in range(m):
    a,b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(*arr)