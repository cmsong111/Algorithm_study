# @ = *3
# % = +5
# # = -7

arr = []

for i in range(int(input())):
    arr = list(map(str,input().split()))
    result = float(arr[0])

    for i1 in range(1,len(arr),1):
        
        if arr[i1] == "@":
            result = result*3
        elif arr[i1] == "%":
            result +=5
        elif arr[i1] == "#":
            result -=7
        

    print("{:.2f}".format(result))