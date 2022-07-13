import sys
input = sys.stdin.readline

x, y = map(int, input().split())

arr1 = []
arr2 = []

for i in range(x):
    temp = list(map(int, input().split()))
    arr1.append(temp)

for i in range(x):
    temp = list(map(int, input().split()))
    arr2.append(temp)

for i in range(0, x, 1):
    for ii in range(0, y, 1):
        print(arr1[i][ii]+arr2[i][ii], end=" ")
    print()
