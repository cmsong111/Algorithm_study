count, target = map(int,input().split())

moneyarr = []

for i in range(count):
    moneyarr.append(int(input()))

result = 0

for i in range(count-1,-1,-1):
    if moneyarr[i] <= target:
        while(moneyarr[i] <= target):
            target-=moneyarr[i]
            result +=1
            #print("현재 금액은",target,"빠진 금액은",moneyarr[i])

print(result)