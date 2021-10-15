<<<<<<< HEAD
num = int(input())
count = 0
while(1):
    if num == 1:
        break
    
    if num % 3 == 1:
        num -=1
        count +=1
        print(num)
        num /=3
        count +=1
        print(num)


    elif num % 3 == 0:
        num = num / 3
        count +=1
        print(num)

    elif num % 2 == 1:
        num = num -1
        count +=1
        print(num)
        num = num / 2
        count +=1
        print(num)

    elif num % 2 == 0:
        num = num / 2
        count +=1
        print(num)

    else:
        num = num - 1
        count +=1
        print(num)
    
    
print(count)
