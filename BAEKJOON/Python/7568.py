standard_input ="""5
55 185
58 183
88 186
60 175
46 155
"""

import sys

#input = sys.stdin.readline

N = int(input())

# 몸무게, 키 , 들어온 순서, 등수
arr = []
for i in range(N):
    a,b = map(int, input().split())
    arr.append([a,b,i+1,1])

arr.sort(key=lambda x: (x[0],x[1]))

for i in range(N):
    for ii in range(N,0,-1):
        if arr[i][0] < arr[ii-1][0] and arr[i][1] < arr[ii-1][1]:
            arr[i][3] += 1
        
arr.sort(key=lambda x: x[2])

# 정답 출력
for i in arr:
    print(i[3], end=" ")
