target = int(input())

arr = list(map(int,input().split()))

result = 0
for i in arr:
    if target == i:
        result+=1
    
print(result)