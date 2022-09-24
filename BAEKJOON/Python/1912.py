import sys

#input = sys.stdin.readline

standard_input = """10
10 -4 3 1 5 6 -35 12 21 -1
"""

count = int(input())

arr = list(map(int, input().split()))


for i in range(1, count):
    arr[i] = max(arr[i], arr[i]+arr[i-1])

print(max(arr))
