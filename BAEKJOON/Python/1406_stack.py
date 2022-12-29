
import sys

standard_input = """abcd
3
P x
L
P y
"""

input = sys.stdin.readline


left = []
right = []

temp = input().rstrip()
for i in temp:
    left.append(i)

testCase = int(input())
# print("초기값")
# print(left,"커서",right)
# print()

for i in range(testCase):
    temp = input().split()
    # print(temp)
    if temp[0] == 'L':
        if left:
            right.append(left.pop())
    elif temp[0] == 'D':
        if right:
            left.append(right.pop())
    elif temp[0] == 'B':
        if left:
            left.pop()
    elif temp[0] == 'P':
        left.append(temp[1])

    # print(left,"커서",right)
    # print()

for i in left:
    print(i, end='')

right.reverse()

for i in right:
    print(i, end='')