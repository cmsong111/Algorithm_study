n = int(input())

arr = [1]*1001

for i in range(2, n+1):
    arr[i] = arr[i-1]+arr[i-2]*2

print(arr[n] % 10007)
