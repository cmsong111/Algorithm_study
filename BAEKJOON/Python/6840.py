standard_input = """10
5
8
"""

arr = []    
for i in range(3):
    arr.append(int(input()))

arr.sort()

print(arr[1])