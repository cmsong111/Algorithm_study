a,b = map(float,input().split())

result = (str(int(a//b))+".")
a = (a % b) * 10

for _ in range(1000): #계속 10씩 곱해주면서 몫을 뒤에 붙여줌
    result += str(int(a // b))
    #print(str(int(a // b)))
    a = (a % b) * 10
    #print(result)
    
print(result)