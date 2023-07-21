import sys
standard_input = """2
3 2 4 2
536874368 268792221 598 1204
"""


# input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a * b > c * d:
        print("TelecomParisTech")
    elif a * b < c * d:
        print("Eurecom")
    else:
        print("Tie")
