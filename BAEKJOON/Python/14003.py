standard_input ="""10
2 -8 6 -2 3 -2 7 7 -8 -9"""

import sys
import bisect


N = int(input())
A = list(map(int, input().split()))

lis_arr = [A[0]]
lis_total = [1] * N

for i in range(1, N):
    
    if lis_arr[-1] < A[i]:
        lis_arr.append(A[i])
        lis_total[i] = len(lis_arr)
    else:
        idx = bisect.bisect_left(lis_arr, A[i])
        lis_arr[idx] = A[i]
        lis_total[i] = idx + 1
    

lis_len = max(lis_total)
print(lis_len)

lis = []
for i in range(N-1, -1, -1):
    if lis_total[i] == lis_len:
        lis.append(A[i])
        lis_len -= 1

print(*lis[::-1])