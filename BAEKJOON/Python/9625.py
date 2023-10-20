standard_input = """10"""

K = int(input())


arr = [[1, 0], [0, 1], [1, 1], [1, 2], [2, 3]]

for i in range(5, K+1):
    arr.append([arr[i-1][0] + arr[i-2][0], arr[i-1][1] + arr[i-2][1]])

print(arr[K][0], arr[K][1])
