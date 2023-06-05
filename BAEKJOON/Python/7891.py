standard_input = """4
-100 100
2 3
0 110101
-1000000000 1"""

testCase = int(input())

for i in range(testCase):
    a, b = map(int, input().split())
    print(a+b)
