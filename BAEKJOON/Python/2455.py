import sys

standard_input = """0 32
3 13
28 25
39 0
"""

# input = sys.stdin.readline

now: int = 0
result: int = 0
inpeople: int = 0
outpeople: int = 0

for i in range(4):
    outpeople, inpeople = map(int, input().split())
    now = now + inpeople - outpeople

    result = max(result, now)

print(result)
