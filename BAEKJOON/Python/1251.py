standard_input = """mobitel"""

input_arr = list(input())

input_len = len(input_arr)
arr = []

for i in range(1,input_len-1):
    for ii in range(i+1,input_len):
        a = input_arr[0:i]
        b = input_arr[i:ii]
        c = input_arr[ii:input_len]

        a.reverse()
        b.reverse()
        c.reverse()

        arr.append("".join(a+b+c))

arr.sort()

print(arr[0])

