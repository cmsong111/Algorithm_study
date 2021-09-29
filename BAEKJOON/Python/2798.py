import itertools

#입력부
a,b = map(int,input().split())
lis = list(map(int,input().split()))


#리스트 추가
num = list(itertools.permutations(lis, 3))
final_list = []

#경우의수 다 찾기
for i in range(len(num)):
    if sum(num[i]) <= b:
        final_list.append(sum(num[i]))

print(max(final_list))
