standard_input = """15
32
48
8
6
"""

import math
#import sys
#input = sys.stdin.readline

total = int(input())
kor = int(input())
mat = int(input())
korcan = int(input())
mathcan = int(input())

kor = math.ceil(kor/korcan)
mat = math.ceil(mat/mathcan)

print(min(total-kor,total-mat))
