import sys
from collections import deque
from itertools import combinations
import copy

standard_input = """8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""
# 0: empty, 1: wall, 2: virus


input = sys.stdin.readline

# print arr
def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()

# count empty space


def count_empty(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                count += 1
    return count

def find_zero_zone(arr):
    zero_zone = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                zero_zone.append([i, j])
    return zero_zone

def build_wall(arr):
    result  =[]
    zero_zone = find_zero_zone(arr)
    for i in combinations(zero_zone, 3):
        temp = []
        for j in i:
            temp.append(j)
        result.append(temp)
    return result
  

# BFS spread virus
def spread_virus(start: list, arr: list):
    BFS_queue = deque()
    BFS_queue.extend(start)

    while BFS_queue:
        position = BFS_queue.popleft()
        x = position[1]
        y = position[0]
        if arr[y][x] == 0:
            arr[y][x] = 2
        if arr[y-1][x] == 0:
            BFS_queue.append([y-1, x])
        if arr[y+1][x] == 0:
            BFS_queue.append([y+1, x])
        if arr[y][x-1] == 0:
            BFS_queue.append([y, x-1])
        if arr[y][x+1] == 0:
            BFS_queue.append([y, x+1])
    
    return arr

def find_virus(arr):
    virus = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                virus.append([i, j])
    return virus


origin_arr = []

y, x = map(int, input().split())

origin_arr.append([1]*(x+2))

for i in range(y):
    temp = [1]
    temp.extend(list(map(int, input().split())))
    temp.append(1)
    origin_arr.append(temp)

origin_arr.append([1]*(x+2))

virus = find_virus(origin_arr)

#################################################

testCase = build_wall(origin_arr)
result = []

while(testCase):
    tc = testCase.pop()
    temp_arr = copy.deepcopy(origin_arr)
    for i in tc:
        temp_arr[i[0]][i[1]] = 1

    temp_arr = spread_virus(virus,temp_arr)
    result.append(count_empty(temp_arr))

print(max(result))