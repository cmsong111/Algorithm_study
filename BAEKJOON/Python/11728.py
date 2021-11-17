a,b = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

for i in a_list:
    b_list.append(i)

b_list.sort()

for i in b_list:
    print(i,end=" ")