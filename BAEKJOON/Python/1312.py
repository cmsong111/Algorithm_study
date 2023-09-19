standard_input = """25 7 5"""

A, B, N = map(int, input().split())

answer = A/B * N**10

answer = int(answer % 10)


print(answer)
