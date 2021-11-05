score = []
for i in range(5):
    temp = list(map(int,input().split()))
    score.append(sum(temp))
# y  = index, x = score
y = score.index(max(score))
x = max(score)

temp = score
temp.sort()
temp.reverse()



if temp[0] != temp[1]:
    print(y+1,x)
