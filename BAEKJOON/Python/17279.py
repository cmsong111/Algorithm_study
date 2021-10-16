a,b = map(int,input().split())

dic = {}
for i in range(a):
    id,password = map(str,input().split())
    dic[id] = password

for i in range(b):
    temp = input()
    print(dic[temp])