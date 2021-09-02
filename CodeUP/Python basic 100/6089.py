a,r,n = map(int, input().split())

result = a

for i in range(1,n):
    result = result * r
print(result)

