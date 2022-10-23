standard_input = """6
SOYOON
"""

count = int(input())
name = input()
result = 0

for i in name:
    result += (ord(i)-64)

print(result)