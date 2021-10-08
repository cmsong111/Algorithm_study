a,b,c, = map(int,input().split())
lis = [a,b,c]
score=0
lis.sort()
if lis[0] == lis[1]:
    if lis[1] == lis[2]:
        score=((10000 + a*1000))
if lis[0]==lis[1]:
    if lis[1]!=lis[2]:
        score=((1000 + lis[0]*100))
if lis[0]!=lis[1]:
    if lis[1]==lis[2]:
        score=((1000 + lis[1]*100))
if lis[0]!=lis[1]:
    if lis[1]!=lis[2]:
        score=(max(lis) * 100)
print(score)