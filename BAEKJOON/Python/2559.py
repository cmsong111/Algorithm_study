import sys

a,b = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

answer = sum(arr[0:b])
temp = answer

for i in range(a-b):

    temp -= arr[i]
    temp += arr[i+b]
    if temp > answer:
        answer = temp


print(answer)