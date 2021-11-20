count = int(input())
result = []

temp = input()

for i in range(len(temp)):
    result.append(temp[i])
    


for i in range(count-1):
    temp = input()
    for i in range(len(result)):
        if result[i] != temp[i]:
            result[i] = "?"
for i in result:
    print(i,end="")
    
