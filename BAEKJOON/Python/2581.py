start_num = int(input())
last_num = int(input())

arr = []
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            arr.append(num)

            

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)