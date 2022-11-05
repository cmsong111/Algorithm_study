standard_input = """3
9 20
23 42
15 37
"""

testCase = int(input())

for _ in range(testCase):
    hour, min = map(int, input().split())

    minAngle1 = min * 6

    hourAngle = hour % 12 * (360/12)
    hourAngle += min * 0.5

    result = 0
    if hourAngle - minAngle1 > 0:
        result = hourAngle - minAngle1
    else:
        result = minAngle1 - hourAngle

    if result < 0:
        result += 180

    elif result > 180:
        result = 360 - result

    print(result)
