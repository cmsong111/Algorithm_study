standard_input = """5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""

n, m, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(int(input()))


BIT = [0] * (n + 1)

def update(i, val):
    while i <= n:
        BIT[i] += val
        i += i & -i

def query(i):
    res = 0
    while i > 0:
        res += BIT[i]
        i -= i & -i
    return res

def queryRange(l:int, r:int):
    #print(query(r), query(l - 1))
    return query(r) - query(l - 1)


for i in range(1, n + 1):
    update(i, arr[i-1])
    

for i in range(m + k):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b, c - arr[b - 1])
        arr[b - 1] = c
    elif a == 2:
        print(queryRange(b, c))

    
