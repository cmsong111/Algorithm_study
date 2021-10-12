num = int(input())

score =[100,100]

for i in range(num):
    a,b = map(int,input().split())
    if a>b:
        score[1]-=a
    elif a<b:
        score[0]-=b

print(score[0])
print(score[1])