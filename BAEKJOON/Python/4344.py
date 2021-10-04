a = int(input())

for i in range(a):
    #변수 초기화
    temp=[]
    real = 0

    temp = list(map(int,input().split()))
    average = (sum(temp)-temp[0])/temp[0]
    for i1 in range(1,temp[0]+1):
        if temp[i1] > average:
            real = real + 1
            
    avg = format((real/temp[0])*100,".3f")
    #avg = "%0.3" % ((real/temp[0])*100,".3f")
    print(avg,"%",end="\n",sep="")