arr = []
setarr = ([])

for i in range(int(input())):
    temp = int(input())
    if temp != 0:
        arr.append(temp)
    else:
        if len(arr) == 0:
            print("결과","0")
            continue
        big = max(setarr)
        small = min(setarr)
        if big > -small:
            print("결과",big)
            del arr[arr.index(max(arr))]
        elif big <= -small:
            print("결과",small)
            del arr[arr.index(min(arr))]
    setarr = (arr)