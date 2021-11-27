a = int(input())

result = 5
temp = 4

for i in range(a-1):
    temp += 3
    result += temp
print(result%45678)
