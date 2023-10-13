standard_input = """2
500 550 4
450 500 7"""

testCase = int(input())

for _ in range(testCase):
    A,B,X = map(int,input().split())
    result = A * (X-1) + B
    print(result)
