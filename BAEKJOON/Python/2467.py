num = int(input())
score = []
for i in range(num):
    a,b,c, = map(int,input().split())
    lis = [a,b,c]
    lis.sort()
    if lis[0] == lis[1]:
        if lis[1] == lis[2]:
            score.append((10000 + a*1000))
    if lis[0]==lis[1]:
        if lis[1]!=lis[2]:
            score.append((1000 + lis[0]*100))
    if lis[0]!=lis[1]:
        if lis[1]==lis[2]:
            score.append((1000 + lis[1]*100))
    if lis[0]!=lis[1]:
        if lis[1]!=lis[2]:
            score.append(max(lis) * 100)

print(max(score))