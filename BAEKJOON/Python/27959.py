standard_input = """30 300"""

a, b = map(int, standard_input.split())

print(a, b)

if (a * 100 <= b):
    print("Yes")
else:
    print("No")
