import sys

standard_input = """8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""

#input = sys.stdin.readline()
#인풋
size = int(input())
arr = []
for i in range(size):
    temp = list(map(int,input().split()))
    arr.append(temp)





#출력용
for i in arr:
    for ii in i:
        print(ii,end ="\t")
    print()