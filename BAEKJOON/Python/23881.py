import sys
arrlen,target =map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
count = 0
#print(arr)

for i in range(arrlen,0,-1):
    #print(i)
    max = 0
    for ii in range(i):
        
        if arr[max] < arr[ii]:
            max = ii
    #print(max,ii)

    if arr[max] != arr[i-1]:
        temp = arr[i-1]
        arr[i-1] = arr[max]
        arr[max] = temp
        count +=1
    
    if count == target:
        print(arr[max],arr[i-1],)
        break
    
   # print(arr)

if target > count:
    print(-1)