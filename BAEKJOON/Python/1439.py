for i in range(int(input())):
    money = int(input())
    temp = 0
    while(money >= 25):
        money -= 25
        temp +=1
    print(temp,end=" ")
    temp = 0
    while(money >= 10):
        money -= 10
        temp +=1
    print(temp,end=" ")
    temp = 0
    while(money >= 5):
        money -= 5
        temp +=1
    print(temp,end=" ")
    temp = 0
    while(money >= 1):
        money -= 1
        temp +=1
    print(temp)