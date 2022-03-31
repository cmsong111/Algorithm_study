a = ""

count, which = map(int,input().split())

for i in range(1,count+1,1):
    a = a+str(i)

result = 0

for i in a:
    if i == str(which):
        result +=1

print(result)