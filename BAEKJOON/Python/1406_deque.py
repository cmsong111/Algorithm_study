from collections import deque
import sys

standard_input = """a
4
L
L
D
P x
"""

input = sys.stdin.readline


left = deque()
right = deque()

temp = input()#.rstrip()
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
            right.appendleft(left.pop())
    elif temp[0] == 'D':
        if right:
            left.append(right.popleft())
    elif temp[0] == 'B':
        if left:
            left.pop()
    elif temp[0] == 'P':
        left.append(temp[1])

    # print(left,"커서",right)
    # print()

for i in left:
    print(i, end='')
for i in right:
    print(i, end='')