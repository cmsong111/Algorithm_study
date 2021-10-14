a = int(input())
num = len(str(a))
i = 0
while(1):
    i+=1
    result = i
    temp = i
    for i1 in range(num):
        result = result + temp % 10
        temp = temp // 10 


    if result == a:
        print(i)
        break

    if i > 1000000:
        print("0")
        break