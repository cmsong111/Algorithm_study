standard_input ="""0
1
1
1
1"""

import sys

def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

# input = sys.stdin.readline

N = int(input())

A = [int(input()) for _ in range(N)]

# 절사 평균 구하기

out_len = my_round(N * 0.15 )

A.sort()

A = A[out_len:N-out_len]

if len(A) == 0:
    print(0)
else:
    print(my_round(sum(A)/len(A)))
