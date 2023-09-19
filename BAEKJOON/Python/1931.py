standard_input = """3
4 4
3 4
2 4"""

N = int(input())

T = []

for _ in range(N):
    T.append(list(map(int, input().split())))

T.sort(key=lambda x: (x[1], x[0]))
room = 0
answer = 0


for i in T:
    if room <= i[0]:
        room = i[1]
        answer += 1

print(answer)
