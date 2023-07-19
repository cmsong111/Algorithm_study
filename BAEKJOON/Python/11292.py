import sys

standard_input = """3
John 1.75
Mary 1.64
Sam 1.81
2
Jose 1.62
Miguel 1.58
5
John 1.75
Mary 1.75
Sam 1.74
Jose 1.75
Miguel 1.75
0"""


# input = sys.stdin.readline

while (True):
    testCase = int(input())
    if testCase == 0:
        break

    max = 0
    maxName = []

    for i in range(testCase):
        a, b = input().split()

        if float(b) > max:
            max = float(b)
            maxName = [a]
        elif float(b) == max:
            maxName.append(a)

    print(' '.join(maxName))
