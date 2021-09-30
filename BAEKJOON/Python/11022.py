count =int(input())

for i in range(count):
    a,b = map(int,input().split())
    print("Case #",i+1,": ",a," + ",b," = ",a+b,sep="")
