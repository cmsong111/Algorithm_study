a,d,n = map(int, input().split())

result = a
for i in range(n):
    result = result + d
print(result-d)

