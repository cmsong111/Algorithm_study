import sys

arr = []
for i in range(7):
    temp = int(sys.stdin.readline().rstrip())
    if temp % 2 == 1:
        arr.append(temp)
    
if arr:
    arr.sort()
    print(sum(arr))
    print(arr[0])
else:
    print(-1)