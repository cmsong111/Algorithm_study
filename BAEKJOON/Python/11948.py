standard_input = """15
21
15
42
15
62
"""

arr1 = []
arr2 = []
for i in range(4):
    arr1.append(int(input()))

for i in range(2):
    arr2.append(int(input()))


arr1.sort()
arr2.sort()

result = sum(arr1[1:])

result += arr2[1]

print(result)
