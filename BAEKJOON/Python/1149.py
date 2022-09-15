standard_input = """8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19
"""

import sys
input = sys.stdin.readline

testCase = int(input())
arr = []
for i in range(testCase):
    R, G, B = map(int, input().split())
    temp = {'R': R, 'B': B, 'G': G, }
    arr.append(temp)

for i in range(1, testCase, 1):
    arr[i]["R"] += min(arr[i-1]["G"],arr[i-1]["B"])
    arr[i]["G"] += min(arr[i-1]["R"],arr[i-1]["B"])
    arr[i]["B"] += min(arr[i-1]["G"],arr[i-1]["R"])

print(min(arr[-1].values()))