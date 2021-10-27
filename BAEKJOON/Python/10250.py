for i in range(int(input())):
    H, W ,N = map(int,input().split())
    temp = N
    tmp = 1

    #층
    if N%H == 0:
        temp = H
    else:
        temp = N%H 
    
    #호수
    if N/H > int(N/H):
        tmp = int(N/H)+1
    else:
        tmp = int(N/H)

    if tmp < 10:
        print(temp,"0",tmp,sep="")
    else:
        print(temp,tmp,sep="")