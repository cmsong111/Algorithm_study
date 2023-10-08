standard_input ="""20"""

import math

max_num = int(input())

if max_num == 1:
    print(0)
    exit()

arr = [True for _ in range(max_num+1)]
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(max_num)+1)):
    if arr[i] == False:
        continue
    for j in range(i*2, max_num+1, i):
        arr[j] = False


prime_arr = [i for i in range(len(arr)) if arr[i] == True]


start = 0
end = 0
count = 0

while start <= end and end < len(prime_arr):
    temp = sum(prime_arr[start:end+1])
    if temp == max_num:
        count += 1
        end += 1
    elif temp < max_num:
        end += 1
    else:
        start += 1

print(count)