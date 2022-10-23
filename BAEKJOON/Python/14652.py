standard_input = "6 4 14"

x, y, target = map(int, input().split())

print(target//y, target % y)
