
arr = []
count = int(input())
for i in range(count):
    arr.append(int(input()))

#산술평균
print("산술평균")
print(round(sum(arr)/count))

#중앙값
print("중앙값")
arr.sort()
print(arr[round(count/2)])

#최빈값
print("#최빈값")
dic_arr = {}
for i in arr:
    i = str(i) 
    if i in dic_arr:
        dic_arr[i] += 1
    else:
        dic_arr[i] = 1

dic_arr_key = sorted(dic_arr.items())

diclen = len(dic_arr_key)
print(dic_arr)
print(dic_arr_key)


if diclen >= 2:
    if dic_arr_key[0][1] == dic_arr_key[1][1]:
        print(dic_arr_key[1][0])
else:
    print(dic_arr_key[0][0])


# if len(key) > 2:
#     if key[0][0] == key[1][0]:
#         print(key[1][0])


#범위
print("범위")
print(arr[count-1] - arr[0])
