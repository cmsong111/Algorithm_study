a,b = map(str, input().split())
al = []
bl = []
for i in range(3):
    al.append(a[i])
for i in range(3):
    bl.append(b[i])

print("리스트 생성 완료")


a = int(al[2])*100 + int(al[1])*10 + int(al[0])
b = int(bl[2])*100 + int(bl[1])*10 + int(bl[0])
print("a,b 변경 완료")


if a>b:
    print(a)
elif a<b:
    print(b)