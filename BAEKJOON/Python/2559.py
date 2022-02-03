import sys

a,b = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

answer = sum(arr[0:b+1])

for i in range(a-b+1):
    temp = sum(arr[i:i+b])
    if temp > answer:
        answer = temp


print(answer)