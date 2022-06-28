import sys

arr_size, testcase = map(int,sys.stdin.readline().split())
arr =[]

# 입력부
for i in range(arr_size):
    arr.append(list(map(int,sys.stdin.readline().split())))

# 누적합 만들기
for i in range(arr_size):
    for ii in range(0,arr_size-1,1):
        arr[i][ii+1] += arr[i][ii]
        
# 계산 파트
for i in range(testcase):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    result = 0
    x1-=1
    y1-=1

    for ii in range(x1,x2,1):
        if y1-1==-1:
            result += arr[ii][y2-1]
        else:
            result += arr[ii][y2-1] - arr[ii][y1-1]

    print(result)