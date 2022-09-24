standard_input = """30 5 51 3"""

# N = 참여 팀
# M = 팀 인원
# a = 총 남은 사람
# k = 준혁이네 남은 인원

N, M, a, K = map(int, input().split())

last = a-K

max = 0
min = 0
if last > 0:
    max = N
else:
    max = N+1

if last / M == last // M:
    min = last//M+1
else:
    min = int(last/M)+2


print(max, min)
