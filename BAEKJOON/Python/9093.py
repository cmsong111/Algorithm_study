import sys

count = int(sys.stdin.readline().strip())




for i in range(count):
    a = list(map(str,sys.stdin.readline().split()))
    for i in a:
        print(i[::-1],end=" ")
    
    print()