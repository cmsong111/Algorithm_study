standard_input = """3
3 2 1
5 .16 4.54
3 3.7 3.6
"""

testCase = int(input())

for i in range(testCase):
    a = list(map(float, input().split()))
    result = 1

    for j in range(3):
        result *= a[j]

    print("$%.2f" % (result))