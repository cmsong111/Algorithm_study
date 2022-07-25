collect = [1, 1, 2, 2, 2, 8]
now = list(map(int, input().split()))

for i in range(6):
    print(collect[i]-now[i], end=" ")
