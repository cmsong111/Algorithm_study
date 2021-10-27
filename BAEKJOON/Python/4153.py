import sys
while(1):
    a,b,c = map(int,sys.stdin.readline().split())
    if a==0 and b ==  0 and c == 0:
        break
    else:
        lis = [a,b,c]
        lis.sort()
        if lis[2]**2 == lis[1]**2 + lis[0]**2:
            print("right")
        else:
            print("wrong")
