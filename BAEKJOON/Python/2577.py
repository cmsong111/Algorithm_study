a = int(input())
b = int(input())
c = int(input())
num = a*b*c
long = len(str(num))
a=[0,0,0,0,0,0,0,0,0,0]

for i in range(long):
    add = num % 10
    a[add] = a[add] + 1

    num = num//10 


for i in range(10):
    print(a[i])