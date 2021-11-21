temp = input()
result = 10

for i in range(1,len(temp)):
    if temp[i] == temp[i-1]:
        result +=5
    else:
        result +=10

print(result)