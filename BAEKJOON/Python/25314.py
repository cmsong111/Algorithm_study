a = int(input())

a //= 4

result = ""
for i in range(a):
    result += "long "

result += "int"

print(result)