standard_input = """11
3
"""

T = int(input())
S = int(input())

even = False

if T % 2 == 0:
    even = True

A1 = 0
A2 = 0

if even:
    A1 = T // 2
    A2 = T // 2

else:
    A1 = T // 2 + 1
    A2 = T // 2


S = S//2

print(A1 + S)
print(A2 - S)
