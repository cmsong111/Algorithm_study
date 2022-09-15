import sys

#input = sys.stdin.readline

standard_input = """1
2
3
4
5
6
7
8
9
10
-1
"""

result = 0
while(1):
    temp = int(input())
    if(temp == -1):
        print(result)
        break
    else:
        result+=temp

