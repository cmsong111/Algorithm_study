count = int(input())
arr = list(map(int, input().split()))
target = int(input())

result = 0

for i in arr:
    if i == target:
        result += 1

print(result)
