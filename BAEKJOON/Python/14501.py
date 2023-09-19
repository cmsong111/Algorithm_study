standard_input = """7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""


N = int(input())

T = []

for _ in range(N):
    T.append(list(map(int, input().split())))

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + T[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + T[i][0]] + T[i][1])

print(dp[0])
