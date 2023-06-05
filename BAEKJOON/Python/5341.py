standard_input = """4
6
0
"""

while True:
    a = input()
    if a == "0":
        break

    # print(a)

    result = 0

    for i in range(int(a)):
        result += i+1

    print(result)
