a,b = map(int,input().split())
result = []
for _ in range(a):
    temp = input()
    result.append(temp)
end = 0
for i in range(b):
    temp = input()
    if temp in result:
        end+=1
print(end)
