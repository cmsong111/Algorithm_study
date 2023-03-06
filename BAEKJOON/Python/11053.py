standard_input = """6
10 20 10 30 20 50
"""

import sys

#input = sys.stdin.readline

len = int(input())
arr = list(map(int, input().split()))

dp = [1] * len

for i in range(1, len):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))