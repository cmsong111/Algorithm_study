standard_input ="""ABCDE
abcde
01234
FGHIJ
fghij"""


arr= []

for i in range(5):
    arr.append(input())


for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i],end="")
        else:
            continue

