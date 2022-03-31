a = input()

arr =[0]*10
for i in a:
    arr[int(i)]+=1
if (arr[9] + arr[6]) % 2 == 1:
    arr[9] = (arr[9] + arr[6]) // 2
    arr[6] = arr[9] + 1
else:
    arr[6] = arr[9] = (arr[9] + arr[6]) // 2

print(max(arr))