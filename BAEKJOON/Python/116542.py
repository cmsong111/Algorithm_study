import sys

n = int(sys.stdin.readline().strip())
dic = {}

for case in range(n):
    temp = int(sys.stdin.readline().strip())
    if temp in dic:
        dic[temp] += 1
    else:
        dic[temp] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])