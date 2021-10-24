arr = []
count = int(input())
for i in range(count):
    x, y =map(int,input().split())
    arr.append([y,x])

arr.sort()

for i in range(count):
    print(arr[i][1],arr[i][0])
