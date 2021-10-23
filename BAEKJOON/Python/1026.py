import sys

num = int(input())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort()
B.sort()
B.reverse()

result = 0

for i in range(num):
    result = result + (A[i]*B[i])

print(result)


