standard_input = "16"

target = int(input())

arr = list(range(0, target+1, 1))

for i in range(1, target+1, 1):
    # arr[i] = min(arr[i], arr[i-1]+1)
    for ii in range(1, i):
        if (ii**2) > i:
            break
        arr[i] = min(arr[i], arr[i-ii**2]+1)

print(arr)

print(arr[target])
