standard_input = """4 7
6 13
4 8
3 6
5 12
"""

N, K = map(int, input().split())

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, input().split())
    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(V + dp[i - 1][j - W], dp[i - 1][j])

print(dp[N][K])