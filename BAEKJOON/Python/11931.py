import sys

arr = []
count = int(sys.stdin.readline().strip())
for i in range(count):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()


for i in range(count-1,-1,-1):
    print(arr[i])