standard_input = """11 59"""

HH, MM = map(int, input().split())

HH -= 9

result = HH*60 + MM

print(result)
