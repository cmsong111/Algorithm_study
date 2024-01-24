standard_input = """5 7
0010000
0111010
1111111
0111010
0010000"""


N, M = map(int, input().split())

for i in range(N):
    text = input()

    for j in range(M):
        print(text[M - j - 1], end='')
    print()

