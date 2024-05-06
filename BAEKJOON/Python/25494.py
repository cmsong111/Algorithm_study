standard_input = """2
1 2 3
3 2 4"""


test_case = int(input())

for _ in range(test_case):
    a, b, c = map(int, input().split())
    print(min(a, b, c))
