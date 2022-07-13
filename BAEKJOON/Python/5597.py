import sys
input = sys.stdin.readline

arr = list(range(1, 31))

for i in range(28):
    temp = int(input())
    arr.remove(temp)

print(arr[0])
print(arr[1])
