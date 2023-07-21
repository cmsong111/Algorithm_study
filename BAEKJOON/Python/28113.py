

standard_input = """10 5 15"""

n, a, b = map(int, input().split())

if a > b:
    print("Bus")
elif a < b:
    print("Subway")
else:
    print("Anything")
