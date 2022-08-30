a, b = map(int, input().split())
result = a * (100-b)
#print(result)
if result >= 10000:
    print(0)
else:
    print(1)
