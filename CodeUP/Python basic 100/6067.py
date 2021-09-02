def num (n):
    if n < 0:
        if n%2==0:
            print("A")
        else:
            print("B")
    else:
        if n%2==0:
            print("C")
        else:
            print("D")

a = int(input())
num(a)
