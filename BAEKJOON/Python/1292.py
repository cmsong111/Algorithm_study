a,b  = map(int,input().split())

arr = []

for i in range(b+1):
    	for ii in range(i):
        		arr.append(i)

result = sum(arr[a-1:b])

print(result)