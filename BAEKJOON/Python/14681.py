a = int(input())
b = int(input())

if a > 0:
    if b > 0:
        print(1)
    if b < 0:
        print(4)
elif a < 0:
    if b > 0:
        print(2)
    if b < 0:
        print(3)
