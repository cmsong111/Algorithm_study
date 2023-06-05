standard_input = """3
2 2
1 5
13 29
"""

import math

testCase = int(input())

for i in range(testCase):
    a, b = map(int, input().split())
    
    up = math.factorial(b)
    down = math.factorial(a) * math.factorial(b-a)

    print(up//down)

