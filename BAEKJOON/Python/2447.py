total = int(input())

arrtemp = ['*']*total
arr = []

for i in range(total):
    arr.append(list(arrtemp))

target = []

temp = 1
while(temp < total):
    target.append(temp)
    temp *= 3


for i in target: #타겟
    for ii in range(i,total,i*3): #X축
        for iii in range(i,total,i*3): #Y축

            for iiii in range(ii,ii+i,1):
                for iiiii in range(iii,iii+i,1):
                    #print("i : ", i,"\t\tii : ", ii, "\tiii : ", iii,"\tiiii : ", iiii,"\tiiiii : ", iiiii)
                    arr[iiii][iiiii] = " "  
                

#출력
for i in arr:
    for ii in i:
        print(ii ,end="")
    print()