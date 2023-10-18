standard_input  ="""7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7"""

import sys

input = sys.stdin.readline


N= int(input())


arr = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1


# DP 뱅글뱅글

for i in range(N-2,-1,-1):
    for j in range(i+1,N):
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1


M = int(input())

for _ in range(M):
    S,E = map(int, input().split())
    print(dp[S-1][E-1])