time = int(input())

A=300
B=60
C=10

if time%10 != 0:
    print(-1)
else:
    print(time//A,time%A//B,time%A%B//C)
