import sys
from collections import deque

vertex, edge = map(int,sys.stdin.readline().split())

grahp =  []
check = [0]*(vertex+1)


for i in range(vertex+1):
    grahp.append([])


for i in range(edge):
    start,end = map(int,sys.stdin.readline().split())
    grahp[start].append(end)
    grahp[end].append(start)
    
# for i in grahp:
#     print(i)
# print("\n\n")




for i in range(1,vertex+1):  
    if check[i] == 0:
        que = deque()
        que.append(grahp[i])

        while(que):
            temp = que.pop()
            # print("temp: ",temp)
            for ii in temp:
                # print("ii = ",ii)
                if check[ii] == 0:
                    que.append(grahp[ii])
                    check[ii] = i

    
#     print("\n\n")        

check.remove(0)

result = 0
zerocount = 0

for i in check:
    if i== 0:
        zerocount+=1
    
result += (len(set(check)))

if zerocount >= 2:
    result+= (zerocount-1)

print(result)