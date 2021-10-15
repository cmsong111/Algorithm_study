a = int(input())
a = 1000-a
count = 0
while(1):
    while(1):
        if a >= 500:
            a -= 500
            count +=1
        if a < 500:
            break
    while(1):
        if a >= 100:
            a -= 100
            count +=1
        if a < 100:
            break
    while(1):
        if a >= 50:
            a -= 50
            count +=1
        if a < 50:
            break
    while(1):
        if a >= 10:
            a -= 10
            count +=1
        if a < 10:
            break
    while(1):
        if a >= 5:
            a -= 5
            count +=1
        if a < 5:
            break
    while(1):
        if a >= 1:
            a -= 1
            count +=1
        if a < 1:
            break
    break
print(count)