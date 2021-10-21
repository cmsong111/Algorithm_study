count = int(input())

lis = [0,1]

if count == 1:
    print("1")
elif count == 2:
    print("1")
else:
    sum = 1
    for i in range(1,count+1,1):
        lis.append(lis[i-1]+lis[i])
    print(lis[count])
      
