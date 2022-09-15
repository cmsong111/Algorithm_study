standard_input = """2
7 1
8589934591 1
"""

import sys
import math


#input = sys.stdin.readline
testCase = int(input())

for _ in range(testCase): 
    a, b = map(int,input().split())
    result = 0
    while(a > 0):
        a //= 2
        result +=1

    print(result+b)
