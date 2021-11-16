import sys
score = []
result = []
for i in range(8):
    score.append(int(sys.stdin.readline().strip()))
temp = []
for i in score:
    temp.append(i)
temp.sort()
temp.reverse()
print(sum(temp[:5]))
for i in range(5):
    result.append(score.index(max(temp))+1)
    temp.pop(temp.index(max(temp)))
result.sort()
for i in result:
    print(i,end=" ")