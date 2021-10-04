temp = 26
if temp < 10:
        sum = temp
elif temp >= 10:
     sum = temp//10 + temp%10

print(sum)

if temp < 10:
    temp = temp*10 + temp
elif temp >= 10:
    temp = ((temp%10)*10 + (sum%10))

print(temp)