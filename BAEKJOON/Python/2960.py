standard_input = "15 12"

result = [0]
count = 0

N, K = map(int, input().split())

arr = list(range(0, N+1, 1))

for i in range(2, N+1, 1):
    if arr[i] != 0:
        result.append(arr[i])
        arr[i] = 0
        count += 1
    # print("disappeard num", i, "count is", count)

    for ii in range(i*2, N+1, i):
        if arr[ii] != 0:
            result.append(arr[ii])
            arr[ii] = 0
            count += 1
            # print("disappeard num",ii,"count is",count)

print(result[K])
