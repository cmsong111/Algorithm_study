a,b = map(int,input().split())

dontsee = []
dontlook = []

for i in range(a):
    dontsee.append(input())
for i in range(b):
    dontlook.append(input())

#시간 초과 뜨는 방식
#for i in range(len(dontsee)):
#        if dontsee[i] in dontlook:
#            dontboth.append(dontsee[i])

#이렇게 쓰는게 더 빨랑
dontboth = list(set(dontlook) & set(dontsee))

print(len(dontboth))
dontboth.sort()
for i in range(len(dontboth)):
    print(dontboth[i])
