import sys

t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
 
n = arr[0]*arr[-1]
print(n)