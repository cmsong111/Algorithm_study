from math import gcd
count = int(input())
arr = list(map(int,input().split()))


for i in range(1,count):
    temp = gcd(arr[i],arr[0])
    print(arr[0]//temp,"/",arr[i]//temp,sep="")
