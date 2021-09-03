
n = int(input())
a = input().split()
d=[] #빈 리스트

for i in range(24):
    d.append(0)

#리스트 숫자형으로 변경
for i in range(n):
    a[i] = int(a[i])
#a리스트 값을 d로 이동
for i in range(n):
    d[a[i]] += 1

for i in range(1,24):
    print(d[i],end=" ")
    
