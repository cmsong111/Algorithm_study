count = input()
result = set(list(map(int,input().split())))

arr = list(result)
arr.sort()

for i in arr:
    print(i,end=" ")