num = int(input())

timer = list(map(int,input().split()))

timer.sort()
result = 0
for i in range(1,num+1,+1):
    result += sum(timer[0:i])

print(result)