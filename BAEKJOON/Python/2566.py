location = [0,0]
value = 0

for i in range(9):
    arr = list(map(int,input().split()))

    for ii in range(9):
        temp = arr[ii]
        if value <= temp:
            location = [i+1,ii+1]
            value = temp

print(value)
print(location[0],location[1])