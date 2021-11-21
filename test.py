import sys
count = int(sys.stdin.readline().strip())

arrlist = list(map(int,sys.stdin.readline().split()))

for i in range(1,count):
    temp = arrlist[i:]
    
    for i1 in range(len(temp)-1,-1,-1):
        if temp[i1] <= arrlist[i-1]:
            del(temp[i1])
    
    try:
        print(temp[0],end=" ")
    except:
        print("-1",end=" ")

print("-1")