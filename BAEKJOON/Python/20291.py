import sys

dic = {}


count = int(sys.stdin.readline().strip())
for i in range(count):
    tmp=[]
    temp = list(sys.stdin.readline().strip().split('.'))
    if temp[1] not in dic:
        dic[temp[1]] = 1
    else:
        dic[temp[1]] += 1
    

sorted_dict = sorted(dic.items(), key = lambda item: item[0])

for i in range(len(sorted_dict)):
    print(sorted_dict[i][0],sorted_dict[i][1])