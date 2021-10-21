from abc import abstractproperty


num = int(input())

array = [[" "]*num for i in range(num)]

for i in range(num):
    array[0][i] = "*"
    array[num-1][i] = "*"
    array[i][0] = "*"
    array[i][num-1] = "*"

for i in range(num):
        array[i][i] = "*"
        array[num-1-i][i] = "*"
    

for i in range(num):
    for i1 in range(num):
        print(array[i][i1],end="")
    print()