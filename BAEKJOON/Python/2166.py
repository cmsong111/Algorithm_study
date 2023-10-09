standard_input ="""4
0 0
0 10
10 10
10 0"""

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


arr.append(arr[0])


plus = 0
minus = 0

for i in range(N):
    plus += arr[i][0] * arr[i+1][1]
    minus += arr[i][1] * arr[i+1][0]

print(round(abs(plus-minus)/2,1))