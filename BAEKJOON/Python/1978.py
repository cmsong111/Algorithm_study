def go (a):
    if a == 1:
        return False
    
    for i in range(2,a//2+1,+1):
        if a % i == 0:
            return False
    return True

count = int(input())
lis = list(map(int,input().split()))



temp = 0

for i in range(len(lis)):
    if go(lis[i]):
        temp += 1

print(temp)
