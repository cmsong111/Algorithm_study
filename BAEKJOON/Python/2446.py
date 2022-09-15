
standard_input = "6"
num = int(input())

for i in range(num):
    print(" "*i, end="")
    print("*"*((num-i)*2-1))

for i in range(num-2, -1, -1):
    print(" "*i, end="")
    print("*"*((num-i)*2-1))
