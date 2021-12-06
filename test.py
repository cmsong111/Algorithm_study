arr = input()
arr_len = len(arr)

result = [0,0]

for i in range(arr_len):
    if arr[i] == "0":
        result[0] += 1
    else:
        result[1] += 1

result[0] //=2
result[1] //=2

    
print("0"*result[0],"1"*result[1],sep="")
