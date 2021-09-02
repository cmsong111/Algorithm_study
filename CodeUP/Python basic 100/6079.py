a = int(input())
sum=0

for i in range(1000):
    sum +=i
    if sum >= a:
        print(i)
        break
