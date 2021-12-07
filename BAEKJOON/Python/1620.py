import sys
arr_len, q_len = map(int,sys.stdin.readline().split())

arr = []
for i in range (arr_len):
    arr.append(sys.stdin.readline().strip())


for i in range(q_len):
    temp = sys.stdin.readline().strip()
    try:
        tmp = int(temp)-1
        print(arr[tmp])
    except:
        print(arr.index(temp)+1)
