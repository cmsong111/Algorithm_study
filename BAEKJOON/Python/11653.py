import sys

a =int(sys.stdin.readline())
if a != 1:  
    i = 2
    while(i != a):
        if a % i == 0:
            print(i)
            a = a // i
            i = 1
        i = i + 1
    print(a)