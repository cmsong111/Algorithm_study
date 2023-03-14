standard_input = """6
-3
4
9
-2
-5
8
2
-1000
-19
0
"""

import sys

#input = sys.stdin.readline

arr = []
count = int(input())

def DP(arr):
    for i in range(1, len(arr)):
        arr[i] = max(arr[i], arr[i] + arr[i-1])
    
    return max(arr)

while(count):
    for i in range(count):
        arr.append(int(input()))

    print(DP(arr))    

    # 다음 단계 진행
    count = int(input())
    arr = []
