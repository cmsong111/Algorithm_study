standard_input = """5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
"""

import sys
from itertools import combinations

# input = sys.stdin.readline

# 0: 빈 칸, 1: 집, 2: 치킨집

M,N = map(int,input().split())

arr = [[] for _ in range(M)]
chicken = []
house = []


for i in range(M):
    arr[i] = list(map(int,input().split()))

for i in range(M):
    for j in range(M):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            house.append((i,j))

def get_distance(house,chicken):
    distance = 0
    for h in house:
        temp = 1000
        for c in chicken:
            temp = min(temp,abs(h[0]-c[0])+abs(h[1]-c[1]))
        distance += temp
    return distance

# 치킨집 중 M개를 고르는 조합
chicken_comb = list(combinations(chicken,N))

result = 999999999999

for i in chicken_comb:
    result = min(result,get_distance(house,i))

print(result)
