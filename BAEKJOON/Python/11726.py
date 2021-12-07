arr= [1,2]

for i in range(2,1001):
    arr.append((arr[i-2]+arr[i-1])%10007)

print(arr[int(input())-1])
